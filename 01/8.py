#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/16 22:32
# @Author  : alison
# @File    : 8.py

## 定义 def xx(params):  return
## 空function
## pass
## 参数检查
## ****返回多个值***
##


import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100,100, 6)
print(x, y)
# 原来返回值是一个tuple！
r = move(100, 100, 60, math.pi / 6)
print(r)

