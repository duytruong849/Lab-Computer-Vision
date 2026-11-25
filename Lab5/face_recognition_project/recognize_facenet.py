import argparse
import sys
from pathlib import Path
import cv2
import numpy as np
import torch
from facenet_pytorch import InceptionResnetV1, MTCNN
from PIL import Image


def load_models(device: torch.device) -> tuple[MTCNN, InceptionResnetV1]:
    mtcnn = MTCNN(
        image_size=160,
        margin=16,
        min_face_size=40,
        thresholds=[0.6, 0.7, 0.7],
        keep_all=True,
        device=device,
    )
    resnet = InceptionResnetV1(pretrained="vggface2").eval().to(device)
    return mtcnn, resnet


@torch.inference_mode()
def extract_embedding(face_tensor: torch.Tensor, resnet: InceptionResnetV1, device: torch.device) -> np.ndarray:
    # face_tensor có shape (3, 160, 160) hoặc (N, 3, 160, 160)
    if face_tensor.ndim == 3:
        face_tensor = face_tensor.unsqueeze(0)
    face_tensor = face_tensor.to(device)
    emb = resnet(face_tensor)
    emb = torch.nn.functional.normalize(emb, p=2, dim=1)
    return emb.cpu().numpy()


def build_known_database(
    mtcnn: MTCNN,
    resnet: InceptionResnetV1,
    known_dir: Path,
    device: torch.device,
) -> dict[str, np.ndarray]:
    if not known_dir.exists():
        raise FileNotFoundError(f"Không tìm thấy thư mục: {known_dir}")

    database: dict[str, np.ndarray] = {}

    for person_dir in sorted(known_dir.iterdir()):
        if not person_dir.is_dir():
            continue

        embeddings: list[np.ndarray] = []
        for img_path in sorted(person_dir.iterdir()):
            if img_path.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"}:
                continue

            try:
                pil_img = Image.open(img_path).convert("RGB")
            except Exception as exc:
                print(f"Cảnh báo: Không đọc được '{img_path}': {exc}", file=sys.stderr)
                continue

            # mtcnn(pil_img) trả về tensor khuôn mặt đã căn chỉnh hoặc None
            aligned_faces = mtcnn(pil_img)
            if aligned_faces is None:
                print(f"Cảnh báo: Không thấy khuôn mặt trong '{img_path}' — bỏ qua.", file=sys.stderr)
                continue

            # Nếu phát hiện nhiều hơn 1 mặt trong ảnh mẫu, bỏ qua để tránh nhầm người
            if aligned_faces.ndim == 4 and aligned_faces.shape[0] != 1:
                print(
                    f"Cảnh báo: '{img_path}' có {aligned_faces.shape[0]} khuôn mặt (cần đúng 1) — bỏ qua.",
                    file=sys.stderr,
                )
                continue

            emb = extract_embedding(aligned_faces, resnet, device)[0]
            embeddings.append(emb)

        if embeddings:
            mean_emb = np.mean(embeddings, axis=0)
            norm = np.linalg.norm(mean_emb)
            if norm > 0:
                mean_emb = mean_emb / norm
            database[person_dir.name] = mean_emb
            print(f"Đã đăng ký '{person_dir.name}' ({len(embeddings)} ảnh mẫu).")

    if not database:
        raise RuntimeError(f"Không tạo được embedding nào từ '{known_dir}'.")

    return database


def match_face(
    emb: np.ndarray,
    database: dict[str, np.ndarray],
    threshold: float = 0.85,
) -> tuple[str, float]:
    best_name = "Unknown"
    best_dist = float("inf")

    for name, ref_emb in database.items():
        # Khoảng cách Euclidean giữa 2 vector đã chuẩn hóa L2 (thường nằm trong khoảng 0.0 -> 2.0)
        dist = float(np.linalg.norm(emb - ref_emb))
        if dist < best_dist:
            best_dist = dist
            best_name = name

    if best_dist > threshold:
        return "Unknown", best_dist
    return best_name, best_dist


def annotate_frame(
    frame_bgr: np.ndarray,
    mtcnn: MTCNN,
    resnet: InceptionResnetV1,
    database: dict[str, np.ndarray],
    threshold: float = 0.85,
    device: torch.device = torch.device("cpu"),
) -> np.ndarray:
    rgb_frame = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb_frame)

    boxes, probs = mtcnn.detect(pil_img)
    if boxes is None:
        return frame_bgr

    aligned_faces = mtcnn.extract(pil_img, boxes, save_path=None)
    if aligned_faces is None:
        return frame_bgr

    embs = extract_embedding(aligned_faces, resnet, device)

    for box, prob, emb in zip(boxes, probs, embs):
        if prob is None or prob < 0.90:
            continue

        x1, y1, x2, y2 = map(int, box)
        name, dist = match_face(emb, database, threshold=threshold)

        is_known = name != "Unknown"
        color = (0, 200, 0) if is_known else (0, 140, 255)
        label = f"{name} (d={dist:.2f})" if is_known else f"Unknown (d={dist:.2f})"

        cv2.rectangle(frame_bgr, (x1, y1), (x2, y2), color, 2)
        cv2.putText(
            frame_bgr,
            label,
            (x1, max(y1 - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            color,
            2,
        )

    return frame_bgr


def run_image(
    mtcnn: MTCNN,
    resnet: InceptionResnetV1,
    database: dict[str, np.ndarray],
    image_path: str,
    output_path: str | None,
    threshold: float,
    device: torch.device,
) -> None:
    frame = cv2.imread(image_path)
    if frame is None:
        print(f"Lỗi: Không đọc được ảnh '{image_path}'.", file=sys.stderr)
        sys.exit(1)

    result = annotate_frame(frame, mtcnn, resnet, database, threshold=threshold, device=device)
    if output_path:
        cv2.imwrite(output_path, result)
        print(f"Đã lưu ảnh kết quả tại '{output_path}'.")

    cv2.imshow("FaceNet - Image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def run_webcam(
    mtcnn: MTCNN,
    resnet: InceptionResnetV1,
    database: dict[str, np.ndarray],
    camera_index: int,
    threshold: float,
    device: torch.device,
) -> None:
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print(f"Lỗi: Không mở được webcam {camera_index}.", file=sys.stderr)
        sys.exit(1)

    print("Đang chạy webcam với FaceNet. Nhấn 'q' để thoát.")
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            result = annotate_frame(frame, mtcnn, resnet, database, threshold=threshold, device=device)
            cv2.imshow("FaceNet - Webcam", result)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


def main() -> None:
    parser = argparse.ArgumentParser(description="Nhận diện khuôn mặt bằng FaceNet (facenet-pytorch)")
    parser.add_argument("--known-dir", type=Path, default=Path("known_faces"))
    parser.add_argument("--image", type=str, default=None)
    parser.add_argument("--output", type=str, default=None)
    parser.add_argument("--camera", type=int, default=0)
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.85,
        help="Ngưỡng khoảng cách Euclidean (càng nhỏ càng khắt khe, thường 0.75–0.95)",
    )
    args = parser.parse_args()

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Đang sử dụng thiết bị: {device}")

    mtcnn, resnet = load_models(device)
    database = build_known_database(mtcnn, resnet, args.known_dir, device)

    if args.image:
        run_image(mtcnn, resnet, database, args.image, args.output, args.threshold, device)
    else:
        run_webcam(mtcnn, resnet, database, args.camera, args.threshold, device)


if __name__ == "__main__":
    main()