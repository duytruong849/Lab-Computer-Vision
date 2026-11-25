# LAB 3 – QUÁ TRÌNH TRIỂN KHAI

## 1. Chuẩn bị môi trường

Sử dụng môi trường Python ảo `.venv` tại thư mục gốc của repository.

Các thư viện cần thiết:

- OpenCV
- NumPy
- Matplotlib
- Scikit-image

## 2. Các bước thực hiện

### 2.1. Thực hành thuật toán Canny

- Đọc và hiển thị ảnh mẫu.
- Áp dụng Gaussian Blur để giảm nhiễu.
- Thực hiện phát hiện biên bằng OpenCV và Scikit-image.
- Quan sát và so sánh kết quả với Sobel và Laplacian.

### 2.2. Khảo sát tham số

- Thay đổi Gaussian Sigma.
- Điều chỉnh ngưỡng thấp và ngưỡng cao.
- Quan sát sự thay đổi của đường biên trên ảnh kết quả.

### 2.3. Thử nghiệm và mở rộng

- Kiểm tra thuật toán trên ảnh nhiễu, ảnh tương phản thấp và ảnh nhiều chi tiết.
- Kết hợp Canny với phép toán hình thái học.
- Sử dụng `findContours()` để phát hiện đường viền và nhận dạng hình dạng.
- Thử nghiệm phát hiện biên trên ảnh màu.
- Tìm hiểu ứng dụng Canny trên video và webcam.

### 2.4. Xây dựng demo trên trình duyệt

Sử dụng HTML, CSS và JavaScript để xây dựng giao diện cho phép:

- Chọn ảnh từ máy tính.
- Điều chỉnh Gaussian Sigma.
- Thay đổi ngưỡng thấp và ngưỡng cao.
- Thực hiện phát hiện biên Canny.
- Hiển thị ảnh gốc và ảnh kết quả.
- Tải ảnh sau khi xử lý.

## 3. Kết quả

Notebook lưu các kết quả trực quan ngay trong từng cell thực thi. Trang HTML cung cấp giao diện demo độc lập để thử nghiệm thuật toán với ảnh do người dùng lựa chọn.