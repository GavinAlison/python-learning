#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 21:59
# @Author  : alison
# @File    : 13.py

# list
#  方法： len、取值、append()、pop()、insert()
# tuple
# 定义: (1,2,)
cls = ['a', 'b', 'c']
print(cls)
print(cls[0])
print(cls[-1])
print(len(cls))
print(cls.append('dd'))
print(cls)
print(cls.pop())
print(cls)
# insert 在指定位置插入指定值，如果指定位置有值，将该值后移
print(cls.insert(-1, 'haha'))
print(cls)
print(cls[-1])
print(cls.insert(0, 's'))
print(cls)
