# !/usr/bin/python3


# from pytesser3 import *
# import ImageEnhance

# image = Image.open('exam.png')

# #使用ImageEnhance可以增强图片的识别率
# enhancer = ImageEnhance.Contrast(image)
# image_enhancer = enhancer.enhance(4)

# print(image_to_string(image_enhancer))

from pytesser import *
from PIL import Image

image = Image.open('exam.png')

print(Image.image_to_string(image))
  # Open image object using PIL print image_to_string(image) # Run tesseract.exe on image fnord print image_file_to_string('fnord.tif') 