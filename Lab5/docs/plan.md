# LAB 5 – NHẬN DIỆN KHUÔN MẶT BẰNG FACENET

## 1. Mục tiêu

Xây dựng chương trình nhận diện khuôn mặt sử dụng mô hình FaceNet, cho phép xác định danh tính những người đã đăng ký thông qua ảnh tĩnh hoặc webcam.

Hệ thống sử dụng MTCNN để phát hiện và căn chỉnh khuôn mặt, kết hợp InceptionResnetV1 để trích xuất đặc trưng khuôn mặt.

## 2. Xác định bài toán

Nhận diện khuôn mặt là bài toán xác định danh tính một người dựa trên các đặc trưng khuôn mặt.

Hệ thống cần thực hiện các nhiệm vụ:
- Phát hiện khuôn mặt trong ảnh hoặc khung hình webcam.
- Trích xuất vector đặc trưng đại diện cho khuôn mặt.
- So sánh đặc trưng với dữ liệu khuôn mặt đã đăng ký.
- Xác định danh tính hoặc trả về Unknown nếu không tìm thấy kết quả phù hợp.

## 3. Dữ liệu sử dụng

Dữ liệu được lưu trong thư mục `known_faces/`, mỗi người có một thư mục riêng chứa ảnh khuôn mặt mẫu.

- Số người được đăng ký: 6.
- Tổng số ảnh mẫu: 60.
- Số ảnh mỗi người: 10.

Dữ liệu bao gồm ảnh của DangKhoa, GiaBao, Khuong, NgocDuy, ThienThu và XuanHuong.

## 4. Phương pháp thực hiện

Hệ thống sử dụng các thành phần chính:

- **MTCNN:** Phát hiện và căn chỉnh khuôn mặt, đưa ảnh về kích thước 160 × 160.
- **InceptionResnetV1 (FaceNet):** Trích xuất vector đặc trưng khuôn mặt gồm 512 chiều, sử dụng trọng số đã được huấn luyện trước trên VGGFace2.
- **Cơ sở dữ liệu đặc trưng:** Lưu vector đặc trưng trung bình đã chuẩn hóa của từng người.
- **Khoảng cách Euclidean:** Đo mức độ khác biệt giữa vector khuôn mặt đầu vào và vector đã đăng ký.
- **OpenCV:** Xử lý ảnh, thu nhận hình ảnh từ webcam và hiển thị kết quả nhận diện.

## 5. Kế hoạch triển khai

1. Chuẩn bị ảnh khuôn mặt mẫu và phân loại theo từng người.
2. Khởi tạo mô hình MTCNN và FaceNet.
3. Phát hiện, căn chỉnh khuôn mặt trong các ảnh mẫu.
4. Trích xuất vector đặc trưng và xây dựng cơ sở dữ liệu khuôn mặt.
5. Xây dựng chức năng so khớp bằng khoảng cách Euclidean.
6. Triển khai nhận diện trên ảnh tĩnh và webcam.
7. Hiển thị kết quả gồm tên người được nhận diện hoặc Unknown, kèm khoảng cách tương ứng.

## 6. Kết quả mong đợi

Chương trình có khả năng:
- Phát hiện khuôn mặt trong ảnh và webcam.
- Nhận diện những người đã đăng ký trong cơ sở dữ liệu.
- Phân biệt người chưa đăng ký bằng nhãn Unknown.
- Hiển thị khung bao quanh khuôn mặt, tên nhận diện và giá trị khoảng cách.
- Lưu ảnh kết quả khi sử dụng chức năng nhận diện ảnh tĩnh và cung cấp đường dẫn đầu ra.

## 7. Phạm vi và giới hạn

Bài thực hành tập trung xây dựng hệ thống nhận diện 6 người đã đăng ký trong dữ liệu mẫu.

Hiệu quả nhận diện có thể bị ảnh hưởng bởi chất lượng ảnh, điều kiện ánh sáng, góc chụp và mức độ hiển thị của khuôn mặt.

Ngưỡng khoảng cách Euclidean mặc định được thiết lập là 0.85. Hệ thống sử dụng mô hình đã được huấn luyện trước, không thực hiện huấn luyện lại mạng nhận diện khuôn mặt.