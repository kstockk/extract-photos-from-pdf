# PDF Image Extractor

This script extracts JPEG images from a PDF file using [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) (`fitz`). It skips specific images (like logos) based on width and height.

## Features

- Extracts only JPEG images
- Skips known logo image (200x24 pixels)
- Outputs images with page and index numbers
- Simple command-line usage

## Requirements

- Python 3.7+
- `PyMuPDF`

## Setup (Recommended: Use a Virtual Environment)

1. **Clone this repository** (or download the script):
    ```bash
    git clone https://github.com/your-username/pdf-image-extractor.git
    cd pdf-image-extractor
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    ```

3. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

```bash
python extract_images.py path/to/your_file.pdf output_directory/
