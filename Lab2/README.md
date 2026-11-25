# LAB 2 – TOÁN TỬ ĐIỂM ẢNH, LỌC TUYẾN TÍNH VÀ LỌC PHI TUYẾN TÍNH

## 1. Giới thiệu

Lab 2 tập trung tìm hiểu và thực hành các phép biến đổi ảnh trong miền không gian, bao gồm:
- **Toán tử điểm ảnh:** Thay đổi độ sáng, thay đổi độ tương phản, biến đổi âm bản, cắt ngưỡng nhị phân.
- **Lọc tuyến tính:** Lọc trung bình (Mean/Box blur), lọc Gaussian, làm sắc nét ảnh (Sharpening).
- **Bài tập nâng cao:** Phát hiện cạnh bằng toán tử Sobel và Prewitt, tự thiết kế các ma trận kernel `3x3`, so sánh định lượng các bộ lọc và khử nhiễu bằng lọc phi tuyến tính (Median Filter, Bilateral Filter).

Bên cạnh notebook Python, bài thực hành còn cung cấp trang web demo `Lab2.html` bằng HTML, CSS và JavaScript để trải nghiệm trực tiếp toàn bộ thuật toán trên trình duyệt.

## 2. Cấu trúc thư mục

```text
Lab2/
├── README.md
├── Lab2.ipynb
├── Lab2.html
├── lab2_pic.jpg
├── docs/
│   ├── plan.md
│   └── implementation.md
└── outputs/
    ├── img_increased_light.jpg
    ├── img_decreased_light.jpg
    ├── img_increased_contrac.jpg
    ├── img_decreased_contrac.jpg
    ├── img_negative.jpg
    ├── img_threshold.jpg
    ├── img_mean_filter.jpg
    ├── img_boxblur_filter.jpg
    ├── img_gaussian.jpg
    ├── img_sharpen.jpg
    ├── img_sharpen_2.jpg
    ├── img_sobel.jpg
    ├── img_prewitt.jpg
    ├── img_k1.jpg ... img_k6.jpg
    ├── comparison_filters.jpg
    └── nonlinear_filter_demo.jpg
```

## 3. Công nghệ sử dụng

| Công nghệ | Vai trò |
|---|---|
| Python | Ngôn ngữ thực hành |
| Pillow (`PIL`) | Đọc/ghi ảnh, biến đổi không gian màu và lọc kernel |
| NumPy | Tính toán ma trận, toán tử điểm ảnh và cửa sổ trượt |
| OpenCV (`cv2`) | Tích chập phát hiện biên, lọc Median, Bilateral và đánh giá độ sắc nét |
| Jupyter Notebook | Môi trường thực hành và trình bày báo cáo |
| HTML / CSS / JavaScript | Giao diện demo tương tác trực tiếp trên trình duyệt |

## 4. Hướng dẫn sử dụng

### 4.1. Thực hành bằng Jupyter Notebook

Cài đặt các thư viện cần thiết:

```bash
python -m pip install opencv-python numpy pillow
```

Mở notebook `Lab2/Lab2.ipynb` và chạy lần lượt các cell từ trên xuống dưới. Toàn bộ ảnh kết quả sẽ được lưu tự động vào thư mục `Lab2/outputs/`.

### 4.2. Chạy demo HTML trên trình duyệt

Mở trực tiếp file `Lab2.html` bằng trình duyệt web bất kỳ:

- Chọn một ảnh từ máy tính (hoặc thêm nhiễu muối tiêu giả lập ngay trên giao diện).
- Lựa chọn phép biến đổi / bộ lọc và điều chỉnh tham số (độ sáng, tương phản, ngưỡng, bán kính lọc hoặc tự nhập ma trận kernel `3x3`).
- Nhấn **Áp dụng xử lý** để xem kết quả so sánh trực tiếp và nhấn **Tải ảnh kết quả** để lưu về máy.

## 5. Tài liệu

- [Kế hoạch thực hiện](docs/plan.md)
- [Quá trình triển khai](docs/implementation.md)
