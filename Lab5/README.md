# LAB 5 – NHẬN DIỆN KHUÔN MẶT BẰNG FACENET

## 1. Giới thiệu

Bài thực hành xây dựng hệ thống nhận diện khuôn mặt sử dụng mô hình FaceNet kết hợp với MTCNN và OpenCV.

Chương trình hỗ trợ nhận diện khuôn mặt từ ảnh tĩnh hoặc webcam, đồng thời xác định những khuôn mặt chưa có trong cơ sở dữ liệu bằng nhãn `Unknown`.

## 2. Công nghệ sử dụng

- **Python:** Ngôn ngữ lập trình chính.
- **PyTorch:** Nền tảng chạy mô hình học sâu.
- **MTCNN:** Phát hiện và căn chỉnh khuôn mặt.
- **FaceNet (InceptionResnetV1):** Trích xuất vector đặc trưng khuôn mặt.
- **OpenCV:** Xử lý ảnh, video và hiển thị kết quả.
- **NumPy:** Xử lý dữ liệu số và vector đặc trưng.

## 3. Cấu trúc thư mục

```text
Lab5/
├── README.md
├── docs/
│   ├── plan.md
│   └── implementation.md
└── face_recognition_project/
    ├── .gitignore
    ├── requirements.txt
    ├── recognize_facenet.py
    └── known_faces/
        ├── DangKhoa/
        ├── GiaBao/
        ├── Khuong/
        ├── NgocDuy/
        ├── ThienThu/
        └── XuanHuong/
```

## 4. Dữ liệu khuôn mặt

Thư mục `known_faces/` chứa dữ liệu khuôn mặt dùng để đăng ký người cần nhận diện.

- Số lượng người: 6.
- Số lượng ảnh tham chiếu: 60.
- Mỗi người có 10 ảnh.

Các thư mục được đặt tên theo danh tính tương ứng. Chương trình sử dụng tên thư mục làm nhãn nhận diện.

## 5. Cài đặt môi trường

Di chuyển vào thư mục dự án:

```bash
cd Lab5/face_recognition_project
```

Tạo môi trường ảo:

```bash
python -m venv .venv
```

Kích hoạt môi trường ảo trên Linux:

```bash
source .venv/bin/activate
```

Cài đặt thư viện:

```bash
pip install -r requirements.txt
```

**Lưu ý:** PyTorch có thể cần thời gian tải và cài đặt. Phiên bản CUDA cần tương thích với phần cứng và môi trường đang sử dụng. Nếu không có GPU phù hợp, chương trình có thể chạy bằng CPU.

## 6. Cách chạy chương trình

Các lệnh dưới đây được thực hiện trong thư mục `face_recognition_project`.

**Nhận diện bằng webcam:**

```bash
python recognize_facenet.py
```

**Nhận diện từ ảnh:**

```bash
python recognize_facenet.py --image input.jpg
```

**Nhận diện và lưu ảnh kết quả:**

```bash
python recognize_facenet.py --image input.jpg --output result.jpg
```

**Thay đổi ngưỡng nhận diện:**

```bash
python recognize_facenet.py --threshold 0.85
```

Nhấn phím `q` để thoát chế độ nhận diện webcam.

## 7. Nguyên lý hoạt động

Quy trình nhận diện gồm các bước:

1. Đọc dữ liệu khuôn mặt đã đăng ký.
2. Sử dụng MTCNN để phát hiện và căn chỉnh khuôn mặt.
3. Sử dụng FaceNet để trích xuất vector đặc trưng.
4. Xây dựng vector đại diện cho từng người.
5. Trích xuất đặc trưng từ khuôn mặt đầu vào.
6. Tính khoảng cách Euclidean để so sánh với dữ liệu đã đăng ký.
7. Xuất tên người được nhận diện hoặc `Unknown`.

## 8. Tài liệu

- [Kế hoạch thực hiện](docs/plan.md)
- [Quá trình triển khai](docs/implementation.md)

## 9. Hạn chế

- Hệ thống chỉ nhận diện những người đã có dữ liệu đăng ký.
- Kết quả có thể bị ảnh hưởng bởi ánh sáng, góc chụp và chất lượng ảnh.
- Ngưỡng nhận diện cần được điều chỉnh phù hợp với dữ liệu thực tế.
- Mô hình FaceNet sử dụng trọng số pretrained, không thực hiện huấn luyện lại trong bài thực hành.

## 10. Kết luận

Bài thực hành áp dụng các mô hình học sâu vào bài toán nhận diện khuôn mặt. Thông qua việc kết hợp MTCNN, FaceNet và OpenCV, chương trình có thể phát hiện, trích xuất đặc trưng và nhận diện khuôn mặt trên ảnh tĩnh cũng như webcam.