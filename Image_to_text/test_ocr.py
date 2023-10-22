import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img_path='Image_to_text/ocr.png'
img = Image.open(img_path)

text = pytesseract.image_to_string(img,lang='fas')
file = open('Image_to_text/test_ocr.txt','w')
file.write(text)
print(text)