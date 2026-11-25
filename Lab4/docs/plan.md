# LAB 4 – PLAN

## 1. Tổng quan

**Tên bài thực hành:** So sánh sự tương đồng của các hình ảnh sử dụng Wavelet, Python.

**Mục tiêu:** Nghiên cứu phương pháp trích xuất đặc trưng hình ảnh bằng biến đổi Wavelet, xây dựng Wavelet Hash và sử dụng khoảng cách Hamming để đánh giá mức độ tương đồng giữa hai hình ảnh.

## 2. Phát biểu bài toán

Cho hai hình ảnh đầu vào, hệ thống thực hiện trích xuất đặc trưng Wavelet và tạo mã băm tương ứng cho từng ảnh. Sau đó, tính khoảng cách Hamming giữa hai mã băm để đánh giá mức độ tương đồng.

- **Đầu vào:** Hình ảnh từ bộ dữ liệu COIL-100 và các cặp ảnh có nhãn tương đồng hoặc không tương đồng.
- **Đầu ra:** Mã băm của từng ảnh, khoảng cách Hamming và kết quả đánh giá mức độ tương đồng.

## 3. Dữ liệu sử dụng

**Dataset:** COIL-100 (Columbia Object Image Library).

- Tổng số ảnh: 7.200.
- Số lượng đối tượng: 100.
- Số ảnh mỗi đối tượng: 72.
- Góc xoay: từ 0° đến 355°, bước 5°.
- Kích thước ảnh: 128 × 128 pixels.
- Định dạng: PNG, chế độ màu RGB.

**Quy tắc gán nhãn cặp ảnh:**

- Label = 1: Hai ảnh thuộc cùng một đối tượng nhưng khác góc xoay.
- Label = 0: Hai ảnh thuộc hai đối tượng khác nhau.

## 4. Kế hoạch thực hiện

### Giai đoạn 1: Khám phá dữ liệu (EDA)

- Kiểm tra số lượng hình ảnh và đối tượng.
- Thống kê số lượng ảnh theo Object ID.
- Khảo sát góc xoay của hình ảnh.
- Kiểm tra kích thước, chế độ màu và định dạng.
- Trực quan hóa một số hình ảnh mẫu.

### Giai đoạn 2: Tiền xử lý dữ liệu

- Đọc hình ảnh từ bộ dữ liệu COIL-100.
- Chuyển đổi ảnh RGB sang Grayscale bằng Pillow.
- Khảo sát ma trận pixel và phân bố cường độ sáng.
- Lưu ảnh Grayscale vào thư mục riêng.

### Giai đoạn 3: Xây dựng tập dữ liệu cặp ảnh

- Xây dựng cặp ảnh tương đồng và không tương đồng.
- Gán nhãn Ground Truth dựa trên Object ID.
- Cân bằng số lượng hai nhóm cặp ảnh.
- Kiểm tra nhãn, dữ liệu thiếu và cặp trùng lặp.
- Lưu tập dữ liệu cặp ảnh dưới định dạng CSV.

### Giai đoạn 4: Trích xuất đặc trưng và xây dựng Wavelet Hash

- Áp dụng biến đổi Wavelet để phân tích hình ảnh.
- Sử dụng Wavelet db4 với mức phân rã phù hợp.
- Lượng tử hóa hệ số Wavelet bằng Gray Code.
- Tạo mã băm biểu diễn đặc trưng của hình ảnh.

### Giai đoạn 5: So sánh và đánh giá

- Tính khoảng cách Hamming giữa các mã băm.
- Xây dựng ngưỡng phân loại mức độ tương đồng.
- Đánh giá bằng các chỉ số Accuracy, Sensitivity, Specificity, Precision và AUC.
- Sử dụng ROC Curve và Confusion Matrix để phân tích kết quả.

### Giai đoạn 6: Thử nghiệm biến thể và phân tích

- Khảo sát phương pháp sử dụng hệ số Wavelet vùng CA3 kết hợp Median.
- So sánh kết quả giữa các phương pháp.
- Phân tích ảnh hưởng của góc xoay đến khả năng nhận diện cặp ảnh tương đồng.

## 5. Công cụ và thư viện

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Pillow
- PyWavelets
- Scikit-learn

## 6. Sản phẩm đầu ra

- Notebook thực hiện toàn bộ quy trình xử lý và thực nghiệm.
- Tập dữ liệu cặp ảnh `image_pairs.csv`.
- Các kết quả thống kê, biểu đồ và chỉ số đánh giá được lưu trong notebook.

## 7. Phạm vi

Bài thực hành tập trung nghiên cứu phương pháp so sánh độ tương đồng hình ảnh dựa trên đặc trưng Wavelet và khoảng cách Hamming, sử dụng bộ dữ liệu COIL-100. Nội dung bao gồm khám phá dữ liệu, tiền xử lý, xây dựng cặp ảnh, trích xuất đặc trưng, tạo mã băm và đánh giá các phương pháp thử nghiệm.
