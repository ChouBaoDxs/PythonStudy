# -*- coding: UTF-8 -*-
from pytesseract import *
from PIL import Image #     打开图片

#       打开图片，返回一个数据流
image=Image.open('OCR_test.png')
# image=Image.open('test.jpg')

text=image_to_string(image,lang='chi_sim')      #使用chi_sim中文字库进行识别   还有一个是eng

# image=Image.open('test.jpg')
# text=image_to_string(image)

print text
















