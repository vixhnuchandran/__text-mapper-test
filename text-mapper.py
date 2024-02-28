import os
import argparse
from PIL import Image
import pytesseract


def process_image(image_path, output_file=None):
    print(f"Processing image: {image_path}")
    image = image_path
    text = pytesseract.image_to_string(image)
    boxes = pytesseract.image_to_boxes(image)

    if output_file:
        with open(output_file, 'w') as f:
            f.write('Recognized Text: ' + text)
            f.write('\n\nBounding Boxes:\n')
            for box in boxes.splitlines():
                box_info =  box.split()
                f.write(f"Word: {box_info[0]}, Coordinates: {box_info[1:5]}\n")
        print(f"Output saved to {output_file}")
    else:
        print('Recognized Text: ', text)
        print('Bounding Boxes: ')
        for box in boxes.splitlines():
            box_info =  box.split()
            print(f"Word: {box_info[0]}, Coordinates: {box_info[1:5]}")


def main():
    parser = argparse.ArgumentParser(description="A simple script for processing images using OCR.")
    parser.add_argument('image_path', help="Path to the image file")
    parser.add_argument('-o', '--output',  help="Path to output file")

    args = parser.parse_args()
    process_image(args.image_path, args.output)
    
if __name__ == "__main__":
    main()

