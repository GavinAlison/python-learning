#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 9:40
# @Author  : alison
# @File    : pickleDemo.py


import pickle  as pk

integers = [1, 2, 3, 4, 5]
# 文件中以ascii格式保存数据
f = open('.\\res\\1.bat', 'wb')
pk.dump(integers, f)
# 文件中以二进制格式保存数据
f = open('.\\res\\2.bat', 'wb')
pk.dump(integers, f, True)

f.close()

import os

size1 = os.stat('.\\res\\1.bat').st_size
size2 = os.stat('.\\res\\2.bat').st_size
print('%d  %d , %.2f%%' % (size1, size2, (size2 + 0.0) / size1 * 100))

#  读出来，也称之为反序列化。
integers = pk.load(open('.\\res\\1.bat', 'rb'))
print(integers)
integers = pk.load(open('.\\res\\2.bat', 'rb'))
print(integers)


