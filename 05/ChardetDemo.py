#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 21:42
# @Author  : alison
# @File    : ChardetDemo.py

import chardet

r = chardet.detect(b'hello world')
print(r)

data = '离离原上草，一岁一枯荣'.encode('gbk')
r = chardet.detect(data)
print(r)

data = '离离原上草，一岁一枯荣'.encode('utf-8')
r = chardet.detect(data)
print(r)

data = '哈哈哈'.encode('gbk')
r = chardet.detect(data)
print(r)

data = '最新の主要ニュース'.encode('euc-jp')
r = chardet.detect(data)
print(r)