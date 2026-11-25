# LAB 4 – IMPLEMENTATION

## 1. Tổng quan triển khai

Bài thực hành được triển khai bằng Python trên Jupyter Notebook với tên file `Wavelet_Image_Similarity4.ipynb`.

Nội dung thực hiện bao gồm khám phá dữ liệu COIL-100, tiền xử lý hình ảnh, xây dựng tập cặp ảnh, trích xuất đặc trưng Wavelet Hash và đánh giá khả năng nhận diện hình ảnh tương đồng.

## 2. Môi trường và thư viện

Các thư viện được sử dụng:

- NumPy: xử lý dữ liệu dạng mảng.
- Pandas: quản lý và thống kê dữ liệu.
- Matplotlib: trực quan hóa hình ảnh và kết quả.
- Pillow: đọc và xử lý hình ảnh.
- PyWavelets: thực hiện biến đổi Wavelet.
- Scikit-learn: hỗ trợ đánh giá mô hình và các chỉ số phân loại.
- IPykernel: hỗ trợ thực thi Jupyter Notebook.

Danh sách thư viện được khai báo trong `requirements.txt`.

## 3. Quá trình triển khai

### 3.1. Khám phá dữ liệu (EDA)

- Thu thập và kiểm tra danh sách hình ảnh COIL-100.
- Thống kê số lượng ảnh theo Object ID.
- Khảo sát các góc xoay từ 0° đến 355°.
- Kiểm tra kích thước, chế độ màu và định dạng hình ảnh.
- Trực quan hóa hình ảnh mẫu tại nhiều góc xoay.

**Kết quả:** Dữ liệu được khảo sát gồm 7.200 hình ảnh, 100 đối tượng và 72 ảnh cho mỗi đối tượng. Các ảnh có kích thước 128 × 128 pixels, định dạng PNG và chế độ màu RGB.

### 3.2. Tiền xử lý hình ảnh

- Đọc hình ảnh bằng Pillow.
- Chuyển đổi ảnh RGB sang Grayscale.
- Kiểm tra ma trận pixel bằng NumPy.
- Khảo sát phân bố cường độ sáng thông qua Histogram.
- Chuyển đổi và lưu ảnh Grayscale vào `processed/grayscale`.

**Kết quả được ghi nhận trong notebook:** 7.200 ảnh được chuyển đổi thành công, không có ảnh lỗi.

### 3.3. Xây dựng tập dữ liệu cặp ảnh

Hai nhóm cặp ảnh được xây dựng:

- Cặp tương đồng: cùng Object ID, khác góc xoay.
- Cặp không tương đồng: khác Object ID.

Quá trình sinh cặp sử dụng `random seed = 42` để hỗ trợ tái lập kết quả. Các cặp ảnh được kiểm tra nhãn, giá trị thiếu, ảnh trùng và lưu dưới định dạng CSV.

**Kết quả:** Tập dữ liệu `outputs/image_pairs.csv` có 20.000 cặp ảnh, gồm 10.000 cặp tương đồng và 10.000 cặp không tương đồng.

### 3.4. Trích xuất đặc trưng Wavelet

- Áp dụng biến đổi Wavelet với Wavelet `db4`.
- Thực hiện phân rã Wavelet ở mức 3.
- Phân tích các hệ số Wavelet để trích xuất đặc trưng hình ảnh.
- Lượng tử hóa hệ số bằng Gray Code 8-bit.
- Xây dựng Wavelet Hash để biểu diễn đặc trưng của từng ảnh.

Notebook cũng khảo sát đặc trưng tại các vùng hệ số khác nhau, trong đó có vùng CA3.

### 3.5. So sánh độ tương đồng

- Tạo mã băm cho từng hình ảnh.
- Sử dụng khoảng cách Hamming để đo sự khác biệt giữa hai mã băm.
- Phân tích phân bố khoảng cách của các cặp ảnh.
- Xác định ngưỡng phân loại dựa trên kết quả hiệu chỉnh.

### 3.6. Đánh giá và thử nghiệm

Các phương pháp được đánh giá thông qua:

- Accuracy và Balanced Accuracy.
- Sensitivity.
- Specificity.
- Precision.
- ROC Curve và AUC.
- Confusion Matrix.

Notebook thực hiện so sánh phương pháp Wavelet Hash đầy đủ với biến thể CA3 kết hợp Median Hash, đồng thời phân tích khả năng nhận diện theo các nhóm góc xoay.

## 4. Kết quả thực nghiệm

Các kết quả được ghi nhận từ notebook:

| Chỉ số | Wavelet Hash đầy đủ | CA3 + Median |
|---|---:|---:|
| Accuracy / Balanced Accuracy | 0.6627 | 0.7528 |
| Sensitivity | 0.6230 | 0.7270 |
| Specificity | 0.7025 | 0.7785 |
| Precision | 0.6768 | 0.7665 |
| AUC | 0.7007 | 0.8190 |
| Ngưỡng | 44.375 | 111 |

Trong phạm vi thử nghiệm được ghi nhận, phương pháp CA3 kết hợp Median đạt kết quả cao hơn phương pháp Wavelet Hash đầy đủ trên các chỉ số được báo cáo.

Đây là kết quả thực nghiệm của notebook, chưa đủ cơ sở để khẳng định phương pháp này luôn tốt hơn trong mọi bộ dữ liệu hoặc điều kiện đánh giá.

## 5. Phân tích ảnh hưởng của góc xoay

Notebook tiếp tục khảo sát tỷ lệ nhận diện cặp ảnh tương đồng theo từng khoảng góc xoay.

Kết quả cho thấy khả năng nhận diện có sự thay đổi giữa các khoảng góc. Tỷ lệ nhận diện không giảm đều theo góc xoay, do đó cần xem xét đặc điểm hình ảnh và mức độ thay đổi góc nhìn khi phân tích kết quả.

## 6. Cấu trúc thư mục

```text
Lab4/
├── docs/
│   ├── plan.md
│   └── implementation.md
├── outputs/
│   └── image_pairs.csv
├── requirements.txt
└── Wavelet_Image_Similarity4.ipynb
```

## 7. Kết luận

Bài thực hành đã triển khai quy trình so sánh độ tương đồng hình ảnh dựa trên biến đổi Wavelet, mã băm và khoảng cách Hamming.

Các nội dung chính gồm khám phá dữ liệu, tiền xử lý ảnh, xây dựng tập cặp ảnh, trích xuất đặc trưng và đánh giá kết quả bằng nhiều chỉ số. Ngoài phương pháp Wavelet Hash đầy đủ, notebook còn thử nghiệm biến thể CA3 kết hợp Median để so sánh hiệu quả.

**Lưu ý về dữ liệu:** Bộ COIL-100 và thư mục ảnh Grayscale `processed/grayscale` là dữ liệu đầu vào/trung gian được notebook sử dụng, không nằm trong cấu trúc thư mục Lab4 hiện tại. Cần chuẩn bị các dữ liệu này theo đường dẫn mà notebook khai báo nếu muốn chạy lại toàn bộ quy trình từ đầu.