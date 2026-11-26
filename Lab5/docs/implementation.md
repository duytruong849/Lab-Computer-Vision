# LAB 5 – IMPLEMENTATION

## 1. Tổng quan triển khai

Bài thực hành xây dựng hệ thống nhận diện khuôn mặt bằng FaceNet, sử dụng thư viện `facenet-pytorch` kết hợp OpenCV.

Chương trình hỗ trợ hai chế độ:
- Nhận diện khuôn mặt từ ảnh tĩnh.
- Nhận diện khuôn mặt trực tiếp thông qua webcam.

## 2. Môi trường và thư viện

Các thư viện được sử dụng trong chương trình:

| Thư viện | Chức năng |
|---|---|
| PyTorch | Chạy các mô hình học sâu |
| facenet-pytorch | Cung cấp MTCNN và InceptionResnetV1 |
| OpenCV | Đọc ảnh, xử lý video và hiển thị kết quả |
| Pillow | Đọc và chuyển đổi ảnh |
| NumPy | Xử lý vector đặc trưng và tính toán khoảng cách |

Chương trình tự động lựa chọn GPU CUDA nếu có, nếu không sẽ sử dụng CPU.

## 3. Quy trình triển khai

### 3.1. Khởi tạo mô hình

Hệ thống khởi tạo hai mô hình:

- MTCNN với kích thước ảnh đầu ra 160 × 160, dùng để phát hiện và căn chỉnh khuôn mặt.
- InceptionResnetV1 sử dụng trọng số pretrained VGGFace2, dùng để trích xuất đặc trưng khuôn mặt.

### 3.2. Xây dựng cơ sở dữ liệu khuôn mặt

Chương trình duyệt qua từng thư mục trong `known_faces/`.

Đối với mỗi ảnh:
1. Đọc ảnh và chuyển sang định dạng RGB.
2. Sử dụng MTCNN để phát hiện và căn chỉnh khuôn mặt.
3. Bỏ qua ảnh không phát hiện được khuôn mặt hoặc có nhiều hơn một khuôn mặt.
4. Đưa khuôn mặt qua InceptionResnetV1 để trích xuất embedding.
5. Chuẩn hóa vector đặc trưng bằng chuẩn L2.

Sau khi xử lý các ảnh của một người, chương trình tính vector trung bình và chuẩn hóa lại để tạo vector đại diện cho người đó.

### 3.3. Nhận diện khuôn mặt

Khi có ảnh đầu vào hoặc khung hình webcam:
1. Chuyển ảnh từ BGR sang RGB.
2. Sử dụng MTCNN phát hiện vị trí các khuôn mặt.
3. Trích xuất và căn chỉnh khuôn mặt.
4. Sử dụng FaceNet để tạo embedding.
5. Tính khoảng cách Euclidean giữa embedding đầu vào và vector đại diện của từng người.
6. Chọn người có khoảng cách nhỏ nhất.

Nếu khoảng cách nhỏ nhất lớn hơn ngưỡng 0.85, chương trình trả về `Unknown`. Ngược lại, chương trình xác định danh tính tương ứng.

### 3.4. Hiển thị kết quả

Chương trình sử dụng OpenCV để:
- Vẽ khung chữ nhật quanh khuôn mặt.
- Hiển thị tên người được nhận diện hoặc nhãn `Unknown`.
- Hiển thị giá trị khoảng cách Euclidean.

Đối với ảnh tĩnh, chương trình hỗ trợ lưu ảnh kết quả nếu người dùng cung cấp đường dẫn đầu ra.

Đối với webcam, chương trình xử lý liên tục các khung hình và cho phép nhấn phím `q` để thoát.

## 4. Cấu trúc chương trình

| Hàm | Chức năng |
|---|---|
| `load_models()` | Khởi tạo MTCNN và FaceNet |
| `extract_embedding()` | Trích xuất và chuẩn hóa vector đặc trưng |
| `build_known_database()` | Xây dựng cơ sở dữ liệu khuôn mặt |
| `match_face()` | So khớp khuôn mặt bằng khoảng cách Euclidean |
| `annotate_frame()` | Phát hiện, nhận diện và chú thích khuôn mặt |
| `run_image()` | Thực hiện nhận diện từ ảnh tĩnh |
| `run_webcam()` | Thực hiện nhận diện qua webcam |
| `main()` | Xử lý tham số và điều khiển chương trình |

## 5. Tham số cấu hình

| Tham số | Giá trị mặc định | Ý nghĩa |
|---|---|---|
| `image_size` | 160 | Kích thước ảnh khuôn mặt |
| `min_face_size` | 40 | Kích thước khuôn mặt tối thiểu |
| `threshold` | 0.85 | Ngưỡng khoảng cách nhận diện |
| `probability` | 0.90 | Độ tin cậy phát hiện tối thiểu khi chú thích |
| `camera` | 0 | Chỉ số webcam mặc định |

## 6. Cách sử dụng chương trình

Chạy chương trình từ thư mục `face_recognition_project`.

**Nhận diện bằng webcam:**

```bash
python recognize_facenet.py
```

**Nhận diện từ ảnh:**

```bash
python recognize_facenet.py --image input.jpg
```

**Nhận diện từ ảnh và lưu kết quả:**

```bash
python recognize_facenet.py --image input.jpg --output result.jpg
```

**Thay đổi ngưỡng nhận diện:**

```bash
python recognize_facenet.py --threshold 0.85
```

## 7. Kết luận

Bài thực hành đã xây dựng quy trình nhận diện khuôn mặt dựa trên MTCNN và FaceNet. Hệ thống sử dụng vector đặc trưng và khoảng cách Euclidean để xác định danh tính, hỗ trợ nhận diện trên ảnh tĩnh và webcam.

Phương pháp này cho phép nhận diện những người đã đăng ký và phân loại các khuôn mặt không phù hợp với dữ liệu tham chiếu thành Unknown.