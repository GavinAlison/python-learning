#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 10:29
# @Author  : alison
# @File    : IODemo.py


'''
io
    StringIO
    ByteIO
'''

from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

f = StringIO('learning python')
print('f.read()==' + f.read())
print('f.read()==' + f.read())
print('f.getvalue()==' + f.getvalue())

from io import BytesIO

f = BytesIO()
f.write('中文'.encode('utf-8'))
print('f.getvalue()==' + str(f.getvalue()))
print(f.getvalue().decode('utf-8'))
