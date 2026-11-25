# IMPLEMENTATION FOR LAB 1

## 1. DIRECTORY TREE

```text
Lab1/
├── assets/
│   └── fonts/
│       └── DejaVuSans.ttf
├── docs/
│   ├── plan.md
│   └── implementation.md
├── outputs/
│   ├── images_graysacled.jpg
│   ├── img_HSV_h.png
│   ├── img_HSV_s.png
│   ├── img_HSV_v.png
│   ├── images_LAB.tif
│   ├── images_sliced.jpg
│   ├── images_resized.jpg
│   ├── img_drawed.jpg
│   └── img_texted.jpg
├── images.jpg
└── Lab1.ipynb
```

## 2. DETAILED IMPLEMENTATION

### 2.1. Environment Setup

- Use Python as the programming language.
- Install Pillow for image processing.
- Use Jupyter Notebook to execute the lab exercises.
- Store the font resource in `assets/fonts/`.

### 2.2. Image Loading and Saving

- Load the input image `images.jpg` using `Image.open()`.
- Access image information such as width, height and format.
- Save the image using Pillow's `save()` method.

### 2.3. Color Space Conversion

Use the `convert()` method to transform the original image into different color spaces:

- **Grayscale:** Convert the image to grayscale using mode `L`.
- **HSV:** Convert the image to HSV and split it into H, S and V channels.
- **LAB:** Convert the image to LAB color space.

Save the resulting images in the `outputs/` directory.

### 2.4. Cropping and Resizing

- Use `crop()` to extract a region from the original image.
- Use `resize()` to change the image dimensions to 800 × 600 pixels.
- Save the processed images in `outputs/`.

### 2.5. Drawing Shapes and Adding Text

Use `ImageDraw` to perform basic image annotation:

- Draw a yellow circle.
- Draw a red horizontal line.
- Draw a blue rectangle.
- Add the text "Hello World!" using the DejaVu Sans font.

Save the resulting images in `outputs/`.

## 3. IMPORTANT NOTES

- The input image `images.jpg` must be available in the Lab1 directory.
- Generated images are stored in the `outputs/` directory.
- The DejaVu Sans font is included in the project to avoid depending on Arial being installed on the system.
- The notebook uses Pillow for image processing.