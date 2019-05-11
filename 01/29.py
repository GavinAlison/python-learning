#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 9:20
# @Author  : alison
# @File    : 16.py

#
try:
    f = open('readme.md', 'r', encoding='utf-8')
    print(f.read())
except Exception as e:
    print(e)
finally:
    if f:
        f.close()
f = open('readme.md', 'r', encoding='utf-8')
f.read(12)
f.readline()
