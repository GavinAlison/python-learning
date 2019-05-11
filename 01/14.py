#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/21 22:08
# @Author  : alison
# @File    : 14.py

from collections import Iterable

# 迭代
# dict
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
print('============')
for value in d.values():
    print(value)
print("============")
for item in d.items():
    print(item)

# 判断迭代
o = isinstance('asd', Iterable)  # str是否可迭代
print(o)
o = isinstance([1, 2, 3], Iterable)  # list是否可迭代
print(o)
o = isinstance(1234, Iterable)  # 整数是否可迭代
print(o)
o = isinstance((1, 2,), Iterable)  # str是否可迭代
print(o)

# enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['a','s','d']):
    print(i, value)

print('-------------')



