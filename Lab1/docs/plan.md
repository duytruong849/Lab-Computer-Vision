# PLAN FOR LAB 1

## 1. OBJECTIVE

Củng cố kỹ năng cơ bản trong xử lý hình ảnh bằng Python và thư viện Pillow.

## 2. REQUIREMENTS

- **Language:** Python 3.X
- **Libraries:**
    - Pillow (`PIL`)
- **Tools:**
    - Jupyter Notebook
    - VSCodium

## 3. TASK BREAKDOWN

1. Cài đặt thư viện và chuẩn bị môi trường
- **Subtask:** Initialize virtual environment.
- **Commands:**
    - Initialize venv:
        - `python -m venv .venv`
        - `source .venv/bin/activate.fish` (For Fish terminal)
    - Install library:
        - `pip install pillow`

2. Đọc và lưu hình ảnh:
- Đọc hình ảnh từ máy tính bằng Pillow.
- Kiểm tra thông tin hình ảnh.
- Lưu hình ảnh với định dạng khác.

3. Chuyển đổi không gian màu:
- Chuyển đổi ảnh RGB sang Grayscale.
- Chuyển đổi ảnh sang HSV và tách ba kênh H, S, V.
- Chuyển đổi ảnh sang không gian màu LAB.

4. Cắt xén và thay đổi kích thước:
- Cắt một vùng hình ảnh bất kỳ.
- Thay đổi kích thước hình ảnh theo kích thước cố định.

5. Vẽ hình cơ bản:
- Vẽ đường thẳng, hình tròn và hình chữ nhật lên ảnh.
- Thêm văn bản vào hình ảnh.

## 4. PROGRESS CHECKLIST

- [x] Prepare Python environment and install Pillow.
- [x] Load and inspect the input image.
- [x] Convert image to Grayscale.
- [x] Convert image to HSV and split H, S, V channels.
- [x] Convert image to LAB color space.
- [x] Crop and resize the image.
- [x] Draw basic shapes on the image.
- [x] Add text using DejaVu Sans font.
- [x] Save and verify all output images.
- [x] Organize project files and documentation.