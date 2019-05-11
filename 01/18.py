#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 9:20
# @Author  : alison
# @File    : 16.py

# 偏函数  functools.partial
print(int('12345'))
#  11 作为2进制转换成10进制
print(int('11', base=2))
print(int('12345', base=10))
print(int('12345', 16))
#  functools.partial
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
import functools

int2 = functools.partial(int, base=2)
r = int2('100000')
print(r)
