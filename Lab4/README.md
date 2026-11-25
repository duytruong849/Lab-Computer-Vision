# LAB 4 – WAVELET IMAGE SIMILARITY

## 1. Giới thiệu

Lab 4 nghiên cứu phương pháp đánh giá độ tương đồng giữa hai hình ảnh bằng biến đổi Wavelet, Wavelet Hash và khoảng cách Hamming.

Bài thực hành sử dụng bộ dữ liệu COIL-100 để khảo sát khả năng nhận diện các hình ảnh thuộc cùng một đối tượng ở những góc xoay khác nhau.

## 2. Mục tiêu

- Khám phá và tiền xử lý bộ dữ liệu COIL-100.
- Chuyển đổi hình ảnh RGB sang Grayscale.
- Xây dựng tập dữ liệu gồm các cặp ảnh tương đồng và không tương đồng.
- Trích xuất đặc trưng bằng biến đổi Wavelet.
- Xây dựng Wavelet Hash và so sánh bằng khoảng cách Hamming.
- Đánh giá kết quả bằng các chỉ số phân loại.
- So sánh Wavelet Hash đầy đủ với biến thể CA3 kết hợp Median.

## 3. Cấu trúc thư mục

```text
Lab4/
├── docs/
│   ├── plan.md
│   └── implementation.md
├── outputs/
│   └── image_pairs.csv
├── requirements.txt
├── README.md
└── Wavelet_Image_Similarity4.ipynb
```

## 4. Công nghệ sử dụng

| Công nghệ / Thư viện | Mục đích |
|---|---|
| Python | Ngôn ngữ lập trình |
| Jupyter Notebook | Môi trường thực nghiệm |
| NumPy | Xử lý mảng và ma trận |
| Pandas | Quản lý dữ liệu |
| Matplotlib | Trực quan hóa |
| Pillow | Xử lý hình ảnh |
| PyWavelets | Biến đổi Wavelet |
| Scikit-learn | Đánh giá kết quả |

Danh sách thư viện được khai báo trong `requirements.txt`.

## 5. Dữ liệu

**Dataset:** COIL-100 (Columbia Object Image Library).

- 7.200 hình ảnh.
- 100 đối tượng.
- 72 hình ảnh cho mỗi đối tượng.
- Kích thước ảnh: 128 × 128 pixels.
- Định dạng: PNG.

Bộ dữ liệu COIL-100 cần được chuẩn bị riêng trước khi chạy lại toàn bộ notebook.

## 6. Phương pháp thực hiện

Quy trình thực nghiệm gồm các bước:

1. Khám phá và thống kê dữ liệu COIL-100.
2. Chuyển đổi ảnh RGB sang Grayscale.
3. Xây dựng các cặp ảnh và gán nhãn.
4. Trích xuất đặc trưng bằng Wavelet db4, mức phân rã 3.
5. Lượng tử hóa hệ số bằng Gray Code 8-bit.
6. Tạo Wavelet Hash và tính khoảng cách Hamming.
7. Xác định ngưỡng phân loại và đánh giá kết quả.
8. Thử nghiệm biến thể CA3 kết hợp Median Hash.
9. Phân tích ảnh hưởng của góc xoay.

## 7. Kết quả thực nghiệm

Kết quả được ghi nhận trong notebook:

| Chỉ số | Wavelet Hash | CA3 + Median |
|---|---:|---:|
| Accuracy / Balanced Accuracy | 0.6627 | 0.7528 |
| Sensitivity | 0.6230 | 0.7270 |
| Specificity | 0.7025 | 0.7785 |
| Precision | 0.6768 | 0.7665 |
| AUC | 0.7007 | 0.8190 |

Trong thử nghiệm này, biến thể CA3 kết hợp Median đạt kết quả tốt hơn trên các chỉ số được báo cáo. Kết quả chỉ phản ánh phạm vi thực nghiệm trong notebook.

## 8. Hướng dẫn cài đặt và thực hiện

### Bước 1: Clone repository

```bash
git clone https://github.com/duytruong849/Lab-Computer-Vision.git
cd Lab-Computer-Vision
```

### Bước 2: Tạo môi trường ảo

```bash
python -m venv .venv
```

Kích hoạt môi trường:

**Linux (Bash):**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### Bước 3: Cài đặt thư viện

```bash
pip install -r Lab4/requirements.txt
```

### Bước 4: Chuẩn bị dữ liệu

Tải bộ dữ liệu COIL-100 và chuẩn bị thư mục dữ liệu theo đường dẫn mà notebook sử dụng.

Cần có dữ liệu ảnh gốc và thư mục ảnh Grayscale đã xử lý trước khi thực hiện đầy đủ các bước tiếp theo.

### Bước 5: Mở Jupyter Notebook

```bash
jupyter notebook Lab4/Wavelet_Image_Similarity4.ipynb
```

Thực hiện các cell theo thứ tự trong notebook.

## 9. Tài liệu

- [Kế hoạch thực hiện](docs/plan.md)
- [Quá trình triển khai](docs/implementation.md)

## 10. Ghi chú

Tập tin `outputs/image_pairs.csv` lưu trữ 20.000 cặp ảnh được sử dụng trong quá trình thực nghiệm.

