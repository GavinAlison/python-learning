#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 23:15
# @Author  : alison
# @File    : 12.py


## 切片
l = ['mical', 'sarah', 'tomas', 'jack']
print(l[0])
print(l[1])
print(l[2])

r = []
n = 3
for i in range(n):
    r.append(l[i])

print(r)

slice = l[:3]
print(slice)  # ['mical', 'sarah', 'tomas']
print(l[0:3])  # ['mical', 'sarah', 'tomas']
print(l[1:3])  # ['sarah', 'tomas']
print(l[10:3])  # []
print(l[-2:])  # ['tomas', 'jack']
print(l[-2:-1])  # ['tomas']
print(l[-2:0])  # []
# -------------------------
list()  # ---> list
# 创建一个数列0-10
lists = list(range(11))
L = list(range(100))
# 前10个数：
L[:10]
# 后10个数：
L[-10:]
# 前11-20个数：
L[10:20]
# 前10个数，每两个取一个
L[:10:2]
# 所有数，每5个取一个：
L[::5]
# 复制一个list：
L[:]

# tuple, 可用于切片
print((0, 1, 2, 3, 4, 5)[:3])
# (0, 1, 2)
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print('ABCDEFG'[:3])
# 'ABC'
print('ABCDEFG'[::2])
# ACEG

