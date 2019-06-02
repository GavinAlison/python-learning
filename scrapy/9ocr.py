#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/30 21:07
# @Author  : alison
# @File    : 9ocr.py


from PIL import Image
import tesserocr

from tesserocr import PyTessBaseAPI

# images = ['sample.jpg', 'sample2.jpg', 'sample3.jpg']

# with PyTessBaseAPI() as api:
#     for img in images:
#         api.SetImageFile(img)
#         print(api.GetUTF8Text())
#         print(api.AllWordConfidences())


# method-1
# image = Image.open('./photo/image.jpg')
# result = tesserocr.image_to_text(image)
# print(result)
# Python3WebSpider

#  二值化
# 利用二值化去除条纹
# 什么是二值化？
# 可以这样去看待图像上的每个像素点：255代表纯黑，0代表纯白，127代表灰，可知比如234就代表比较黑，34代表挺白的......
# 我们将 [0 ~ 127] 的偏白的像素全部不要，将 [127 ~ 255] 的偏黑的像素全部保留，这样就没有灰色的线条干扰了，就可以提高识别率了
# 图像的二值化，就是将图像上的像素点的灰度值设置为0或255，

# print(tesserocr.file_to_text('./photo/code.jpg'))
# 无输出
def convertTwoValue(path):
    image = Image.open(path)
    # 转化为灰度图像
    image = image.convert('L')
    threshold = 127
    table = []
    for i in range(256):
        if i < threshold:
            # 去除偏白的像素
            table.append(0)
        else:
            # 保留偏黑的像素
            table.append(1)
    image = image.point(table, '1')
    # image.show()
    return image

imagePath = './photo/code.jpg'
image = convertTwoValue(imagePath)
# image.show()
# value = tesserocr.image_to_text(image)
# print(value)
# print(tesserocr.file_to_text(imagePath))

# tesseract_cmd = ""
import pytesseract
val = pytesseract.image_to_string(Image.open(imagePath))
print(val)

# method-2


