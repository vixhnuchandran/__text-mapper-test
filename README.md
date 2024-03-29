# Text Mapper

Text Mapper is a Python script for processing images using Optical Character Recognition (OCR) to extract text and bounding box coordinates.

## Requirements

- Python 3.x
- pytesseract
- PIL (Python Imaging Library)
- argparse

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/vixhnuchandran/text-mapper.git
   ```

2. Change directory
   ```bash
   cd text-mapper/
   ```
3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python text-mapper.py image_path [-o OUTPUT_FILE]
```

- image_path: Path to the input image file.
- -o, --output: Optional. Path to the output text file where the recognized text and bounding box coordinates will be saved.

Example:

```bash
python text-mapper.py sample_image.jpg -o output.txt
```

#### Output

The script outputs the recognized text and bounding box coordinates. If an output file is specified, the information is saved to that file.

## Acknowledgments

- `pytesseract`: Python interface to Google's Tesseract-OCR Engine.
- `PIL (Python Imaging Library)`: Python Imaging Library adds image processing capabilities to your Python interpreter.
- `argparse`: The argparse module makes it easy to write user-friendly command-line interfaces.
