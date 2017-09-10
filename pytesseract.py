# !/usr/bin/python3

from PIL import Image
import pytesseract

#pytesseract.pytesseract.tesseract_cmd = '/opt/local/bin/'
# Include the above line, if you don't have tesseract executable in your PATH
# Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
img = Image.open('exam.png')
# print(pytesseract.image_to_string(Image.open('test.png')))
#print(pytesseract.image_to_string(Image.open('exam.png'), lang='eng'))
print(img)