# LAB 2 – KẾ HOẠCH THỰC HIỆN

## 1. Mục tiêu

Tìm hiểu và thực hành các kỹ thuật xử lý ảnh cơ bản và nâng cao trong miền không gian: toán tử điểm ảnh, lọc tuyến tính, phát hiện cạnh và lọc phi tuyến tính.

## 2. Nội dung thực hiện

### I. Toán tử điểm ảnh (Point Operators)
- **Thay đổi độ sáng:** Tăng hoặc giảm độ sáng của toàn bộ hình ảnh bằng cách cộng hoặc trừ một giá trị cố định cho mỗi điểm ảnh.
- **Thay đổi độ tương phản:** Tăng hoặc giảm độ tương phản bằng cách nhân mỗi điểm ảnh với một hằng số.
- **Biến đổi âm bản:** Đảo ngược các giá trị điểm ảnh (`255 - I`) để tạo ra ảnh âm bản.
- **Cắt ngưỡng (Thresholding):** Tạo ảnh nhị phân bằng cách so sánh giá trị mỗi điểm ảnh với một ngưỡng nhất định (`T = 128`).

### II. Lọc tuyến tính (Linear Filtering)
- **Lọc trung bình (Mean / Box Filter):** Làm mờ ảnh bằng cách tính giá trị trung bình của các điểm ảnh trong một vùng lân cận.
- **Lọc Gaussian (Gaussian Filter):** Làm mờ ảnh một cách tự nhiên hơn bằng cách sử dụng kernel Gaussian.
- **Làm sắc nét (Sharpening):** Tăng cường các cạnh và chi tiết trong ảnh bằng cách sử dụng các kernel làm sắc nét thích hợp.

### III. Bài tập nâng cao
- **Phát hiện cạnh:** Sử dụng các kernel Sobel và Prewitt theo hai hướng X, Y để phát hiện các cạnh trong ảnh.
- **Tự thiết kế kernel:** Tạo 6 kernel tùy chỉnh (`3x3`) để đạt được các hiệu ứng khác nhau (chạm nổi Emboss, nhấn biên theo hướng, biên chéo, Laplacian).
- **So sánh các loại lọc:** So sánh hiệu quả trực quan và định lượng (độ sắc nét Laplacian, sai số MAE) của các bộ lọc khác nhau trên cùng một hình ảnh.
- **Áp dụng lọc phi tuyến tính:** Tìm hiểu và thực nghiệm khử nhiễu muối tiêu bằng **Median filter** và **Bilateral filter**.

## 3. Công cụ và thư viện

- Python 3.x
- Pillow (`PIL`)
- NumPy
- OpenCV (`cv2`)
- Jupyter Notebook
- HTML, CSS và JavaScript cho phần demo trực tiếp trên trình duyệt.

## 4. Sản phẩm đầu ra

- Notebook thực hành `Lab2.ipynb`.
- Thư mục `outputs/` lưu trữ toàn bộ các ảnh kết quả và ảnh ghép so sánh.
- Trang demo tương tác `Lab2.html` chạy trực tiếp trên trình duyệt.
- Tài liệu kế hoạch (`docs/plan.md`) và quá trình triển khai (`docs/implementation.md`).
