#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 9:20
# @Author  : alison
# @File    : 16.py

# StringIO  , BytesIO
from io import StringIO
from io import BytesIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

f1 = StringIO('1\n2\n3\n')
while True:
    s = f1.readline()
    if s == '':
        break
    print(s.strip())

f3 = BytesIO()
f3.write('中文'.encode('utf-8'))
print(f3.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
