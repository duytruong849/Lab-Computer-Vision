# LAB 2 – QUÁ TRÌNH TRIỂN KHAI

## 1. Chuẩn bị môi trường

Các thư viện Python cần thiết để chạy notebook `Lab2.ipynb`:

- `Pillow` (`PIL`)
- `NumPy`
- `OpenCV` (`opencv-python`)

Tất cả ảnh kết quả sinh ra từ notebook được gom gọn vào thư mục `outputs/` thông qua `OUTPUT_DIR = Path("outputs")`.

## 2. Các bước thực hiện

### 2.1. Toán tử điểm ảnh (Point Operators)

- **Thay đổi độ sáng:** Chuyển ảnh sang mảng `int16`, cộng/trừ `20` đơn vị cho từng pixel, giới hạn trong đoạn `[0, 255]` bằng `np.clip` và lưu thành `img_increased_light.jpg`, `img_decreased_light.jpg`.
- **Thay đổi độ tương phản:** Nhân mảng ảnh kiểu `float32` với hệ số `1.5` (tăng tương phản) và `0.3` (giảm tương phản), dùng `np.clip` về `[0, 255]` rồi lưu thành `img_increased_contrac.jpg`, `img_decreased_contrac.jpg`.
- **Biến đổi âm bản:** Tính `255 - img` trên từng kênh màu RGB và lưu thành `img_negative.jpg`.
- **Cắt ngưỡng:** Chuyển ảnh sang mức xám (`L`), áp dụng ngưỡng `T = 128` bằng `np.where(img_gray >= T, 255, 0)` để tạo ảnh nhị phân `img_threshold.jpg`.

### 2.2. Lọc tuyến tính (Linear Filtering)

- **Lọc trung bình:**
  - Tự cài đặt phép tính trung bình vùng lân cận `3x3` bằng kỹ thuật trượt cửa sổ vector hóa trên NumPy (`np.pad` + tổng 9 vùng dịch chuyển chia `9.0`), lưu thành `img_mean_filter.jpg`.
  - Thực hiện đối chiếu với hàm có sẵn `ImageFilter.BoxBlur(1)` của Pillow, lưu thành `img_boxblur_filter.jpg`.
- **Lọc Gaussian:** Áp dụng `ImageFilter.GaussianBlur(radius=10)` để làm mờ tự nhiên và lưu thành `img_gaussian.jpg`.
- **Làm sắc nét:** Sử dụng `ImageFilter.Kernel` với 2 ma trận `3x3` có trọng số tâm lần lượt là `5` (4 lân cận `-1`) và `9` (8 lân cận `-1`), lưu thành `img_sharpen.jpg` và `img_sharpen_2.jpg`.

### 2.3. Bài tập nâng cao

- **Phát hiện cạnh (Sobel & Prewitt):**
  - Chuyển ảnh gốc sang ảnh xám kiểu `float32`.
  - Áp dụng tích chập 2 chiều bằng `cv2.filter2D(..., cv2.CV_32F, ...)` với cặp kernel `Kx`, `Ky` của **Sobel** và **Prewitt** để giữ nguyên cả đạo hàm âm và dương.
  - Tính biên độ gradient tổng hợp `G = np.sqrt(Gx**2 + Gy**2)` và chuẩn hóa về `[0, 255]`, lưu thành `img_sobel.jpg` và `img_prewitt.jpg`.
- **Tự thiết kế kernel:**
  - Thiết kế 6 kernel `3x3` tùy chỉnh (`Kernel_1` đến `Kernel_6`) tạo hiệu ứng chạm nổi (Emboss), nhấn cạnh định hướng (phải, trái, trên, chéo) và lọc Laplacian, xuất ra `img_k1.jpg` đến `img_k6.jpg`.
- **So sánh các loại lọc:**
  - Áp dụng độc lập các bộ lọc `Mean (5x5)`, `Gaussian (5x5)`, `Median (5x5)` và `Bilateral` lên cùng ảnh gốc.
  - Tính phương sai Laplacian (đo độ sắc nét) và MAE so với ảnh gốc, đồng thời ghép ảnh trực quan lưu tại `outputs/comparison_filters.jpg`.
- **Áp dụng lọc phi tuyến tính (Median & Bilateral):**
  - Tạo nhiễu muối tiêu giả lập (`4%` số pixel) trên ảnh gốc.
  - Khử nhiễu độc lập bằng `cv2.medianBlur` và `cv2.bilateralFilter`, đánh giá sai số `MSE` và xuất ảnh minh họa `outputs/nonlinear_filter_demo.jpg`.

### 2.4. Xây dựng demo trên trình duyệt (`Lab2.html`)

Sử dụng HTML, CSS và JavaScript thuần (Canvas 2D API) để xây dựng giao diện cho phép:

- Chọn ảnh bất kỳ từ máy tính.
- Chọn nhóm chức năng xử lý ảnh tương ứng với 3 phần của Lab 2:
  - **Toán tử điểm ảnh:** Độ sáng, độ tương phản, âm bản, cắt ngưỡng.
  - **Lọc tuyến tính:** Lọc trung bình, lọc Gaussian, làm sắc nét (tâm 5 và tâm 9).
  - **Nâng cao & Phi tuyến:** Phát hiện cạnh Sobel, Prewitt, Laplacian, chạm nổi Emboss, kernel tùy chỉnh `3x3`, lọc trung vị (Median), lọc song phương (Bilateral) và thêm nhiễu muối tiêu để thử nghiệm.
- Điều chỉnh các tham số trực quan (mức sáng, hệ số tương phản, ngưỡng T, kích thước kernel, sigma, ma trận `3x3` tùy chỉnh).
- Hiển thị song song ảnh gốc và ảnh sau xử lý kèm thông số thời gian thực thi.
- Tải ảnh kết quả về máy tính.

## 3. Kết quả

- Toàn bộ 21 ảnh kết quả được lưu gọn trong `Lab2/outputs/`.
- Notebook `Lab2.ipynb` chạy hoàn chỉnh, nhanh và lưu sẵn bảng số liệu + ảnh so sánh.
- Trang `Lab2.html` hoạt động độc lập trên trình duyệt mà không cần cài đặt server phụ trợ.
