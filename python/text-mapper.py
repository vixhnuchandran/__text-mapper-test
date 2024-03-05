import os
import argparse
from PIL import Image
import pytesseract
import cv2

def process_image(image_path, output_file=None):
    print(f"Processing image: {image_path}")
    
    image = cv2.imread(image_path)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    
    boxes = pytesseract.image_to_boxes(binary)
    
    for box in boxes.splitlines():
        box_info = box.split()
        x, y, w, h = map(int, box_info[1:5])  
        
        cv2.rectangle(image, (x, image.shape[0] - y), (w, image.shape[0] - h), (0, 0, 255), 1)
        

    
    if output_file:
        cv2.imwrite(output_file, image)
        print(f"Output image with bounding boxes saved to {output_file}")
    else:
        cv2.imshow("Image with bounding boxes", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser(description="A simple script for processing images using OCR.")
    parser.add_argument('image_path', help="Path to the image file")
    parser.add_argument('-o', '--output',  help="Path to output image file")

    args = parser.parse_args()
    process_image(args.image_path, args.output)
    
if __name__ == "__main__":
    main()
