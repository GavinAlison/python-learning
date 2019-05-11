#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 9:20
# @Author  : alison
# @File    : 16.py

# type()
# 先定义函数
def fn(self, name='world'):
    print('hello , %s' %name)
# 创建Hello class
Hello = type('Hello', (object,), dict(hello=fn))
h = Hello()
print(h)


