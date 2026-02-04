# Image Converter App

Simple and fast image optimizer to convert PNG, JPG, and JPEG images to WebP format.

## Setup

1.  Python must be installed on your system.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Put your images (`.png`, `.jpg`, `.jpeg`) inside the **`to-convert`** folder.
2.  Run the script:
    ```bash
    python converter.py
    ```
3.  Find your optimized images in the **`converted`** folder.

## Features

-   **Parallel Processing**: Uses all CPU cores for fast batch conversion.
-   **Smart Optimization**: Reduces file size while maintaining high visual quality (WebP).
-   **Simple Workflow**: Just drag & drop and run.
