import os
from PIL import Image
import pytesseract

script_dir = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(script_dir, '..', 'images', 'sample.jpg')

image = Image.open(image_path)

text = pytesseract.image_to_osd(image)
boxes = pytesseract.image_to_boxes(image)

print('Recognized Text: ', text)
print('Bounding Boxes: ')
for box in boxes.splitlines():
    box_info =  box.split()
    print(f"Word: {box_info[0]}, Coordinates: {box_info[1:5]}")