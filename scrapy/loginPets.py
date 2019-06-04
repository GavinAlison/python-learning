#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/2 10:19
# @Author  : alison
# @File    : loginPets.py


from urllib.request import urlretrieve
from PIL import Image
import tesserocr


# 二值化
def convertTwoValue(path):
    image = Image.open(path)
    # 转化为灰度图像
    image = image.convert('L')
    threshold = 126
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

    # img = './photo/1'
    # url = 'https://member.etest.net.cn/login/createCode'
    # urlretrieve(url, img + '.jpg')
    # imgPath = img + ".jpg"
    # image = Image.open(img + '.jpg')
    # image.show()

    # image = convertTwoValue(imgPath)
    # image.show()
    # val = tesserocr.image_to_text(image)
    # print(val)

    # from claptcha import Claptcha
    # c = Claptcha("1001", r'./font/freemonotengwar.otf')
    # text, _file = c.write('./photo/2.jpg')
    # print(text, _file)
    # c2 = Claptcha("A4oO0zZ2", "./font/freemonotengwar.otf")
    # text, _file = c2.write('./photo/3.png')
    # print(text, _file)


"""传入二值化后的图片进行降噪"""
'''八邻域算法：8邻域就是判断周围8个像素点。
如果这8个点中255的个数大于某个阈值则判断这个点为噪音，阈值可以根据实际情况修改。'''


# def depoint(img):
#     pixdata = img.load()
#     w, h = img.size
#     print(w, h)
#     for y in range(1, h - 1):
#         for x in range(1, w - 1):
#             count = 0
#             if pixdata[x, y-1] > 245:  # 上
#                 count = count + 1
#             if pixdata[x, y + 1] > 245:  # 下
#                 count = count + 1
#             if pixdata[x - 1, y] > 245:  # 左
#                 count = count + 1
#             if pixdata[x + 1, y] > 245:  # 右
#                 count = count + 1
#             if pixdata[x - 1, y - 1] > 245:  # 左上
#                 count = count + 1
#             if pixdata[x - 1, y + 1] > 245:  # 左下
#                 count = count + 1
#             if pixdata[x + 1, y - 1] > 245:  # 右上
#                 count = count + 1
#             if pixdata[x + 1, y + 1] > 245:  # 右下
#                 count = count + 1
#             if count > 6:  # 控制领域判定大小
#                 pixdata[x, y] = 255
#     return img
#
# imagePath = './photo/3.png'
# image = Image.open(imagePath)
# image = depoint(image)
# val = tesserocr.image_to_text(image)
# print(val)

def book_clear(image, threshold):
    image = image.convert("L")
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    img = image.point(table, "1")
    # img.save("./photo/img1.png")
    # img.show()
    result = tesserocr.image_to_text(img)
    print('灰度二值化之后：' + result)
    return img


def depoint(img2):
    """传入二值化后的图片进行降噪"""
    img2 = img2.convert(mode='L')
    pixdata = img2.load()  # 加载图片数据
    w, h = img2.size
    print(w, h)
    # print(pixdata[1, 1])
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            count = 0
            if pixdata[x, y - 1] > 245:
                count = count + 1
            if pixdata[x, y + 1] > 245:
                count = count + 1
            if pixdata[x - 1, y] > 245:
                count = count + 1
            if pixdata[x + 1, y] > 245:
                count = count + 1
            if pixdata[x - 1, y - 1] > 245:
                count = count + 1
            if pixdata[x - 1, y + 1] > 245:
                count = count + 1
            if pixdata[x + 1, y - 1] > 245:
                count = count + 1
            if pixdata[x + 1, y + 1] > 245:
                count = count + 1
            if count > 6:  # 控制领域判定大小
                pixdata[x, y] = 255
    # img2.save("./photo/img2.png")
    # img.show()
    result = tesserocr.image_to_text(img2)
    print('八领域降噪之后：' + result)
    return img2


# imagePath = './photo/zao.png'
# img = Image.open(imagePath)
# book_clear(img, 127)  # 灰度化+二值化
# img2 = Image.open(imagePath)
# eight_img = depoint(img2)

codePath = './photo/createCode.jpg'
image = Image.open(codePath)
image = book_clear(image, 127)
image = depoint(image)
image.show()
val = tesserocr.image_to_text(image)
print(val)


#  总结tessertocr 的识别率不高，对于简单的文字可以正确识别，
# 对于有早点的字符无法识别， 二值化和降噪都是无法识别字符

