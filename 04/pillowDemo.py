#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 20:46
# @Author  : alison
# @File    : pillowDemo.py

from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('12.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnail((w // 2, h // 2))
print('Resize image to: %sx%s' % (w // 2, h // 2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')

im = Image.open('12.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
