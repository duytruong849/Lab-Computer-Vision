# LAB 3 – PHÁT HIỆN BIÊN CANNY (CANNY EDGE DETECTOR)

## 1. Giới thiệu

Lab 3 tập trung tìm hiểu và thực hành thuật toán phát hiện biên Canny trong xử lý ảnh số.

Bài thực hành sử dụng Python kết hợp OpenCV và Scikit-image để phân tích, phát hiện đường biên trên ảnh. Ngoài ra, bài còn xây dựng một trang demo bằng HTML, CSS và JavaScript cho phép người dùng tải ảnh và thử nghiệm thuật toán Canny trực tiếp trên trình duyệt.

## 2. Nội dung thực hiện

- Tìm hiểu nguyên lý và các giai đoạn của thuật toán Canny.
- Phát hiện biên bằng OpenCV và Scikit-image.
- So sánh Canny với Sobel và Laplacian.
- Khảo sát ảnh hưởng của Gaussian Sigma và ngưỡng phát hiện biên.
- Thử nghiệm trên ảnh nhiễu, ảnh tương phản thấp và ảnh nhiều chi tiết.
- Kết hợp Canny với xử lý hình thái học và phát hiện đường viền.
- Xây dựng demo Canny trên trình duyệt.

## 3. Cấu trúc thư mục

```text
lab3/
├── README.md
├── Lad_3.ipynb
├── Lab3.html
└── docs/
    ├── plan.md
    └── implementation.md
```

## 4. Công nghệ sử dụng

| Công nghệ | Vai trò |
|---|---|
| Python | Ngôn ngữ thực hành |
| OpenCV | Xử lý ảnh và phát hiện biên |
| NumPy | Xử lý dữ liệu ảnh |
| Matplotlib | Hiển thị kết quả |
| Scikit-image | Cung cấp ảnh mẫu và thuật toán xử lý ảnh |
| Jupyter Notebook | Môi trường thực hành |
| HTML/CSS/JavaScript | Xây dựng giao diện demo |

## 5. Hướng dẫn sử dụng

### 5.1. Thực hành bằng Jupyter Notebook

Tại thư mục gốc repository, kích hoạt môi trường ảo:

```bash
source .venv/bin/activate
```

Cài đặt thư viện nếu môi trường chưa có:

```bash
python -m pip install opencv-python numpy matplotlib scikit-image
```

Mở notebook:

```bash
jupyter notebook lab3/Lad_3.ipynb
```

Thực hiện lần lượt các cell để xem nội dung và kết quả.

### 5.2. Chạy demo HTML

Mở file `Lab3.html` trực tiếp bằng trình duyệt:

```bash
xdg-open lab3/Lab3.html
```

Chọn ảnh từ máy tính, điều chỉnh các tham số Sigma, ngưỡng thấp và ngưỡng cao, sau đó nhấn **Chạy Canny** để xem kết quả.

## 6. Tài liệu

- [Kế hoạch thực hiện](docs/plan.md)
- [Quá trình triển khai](docs/implementation.md)

## 7. Kết quả

Bài thực hành cung cấp hai hình thức trải nghiệm:

- Notebook Python với các nội dung thực hành và kết quả trực quan.
- Trang demo HTML cho phép thử nghiệm phát hiện biên Canny trên ảnh tùy chọn.