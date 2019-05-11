#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 20:49
# @Author  : alison
# @File    : strDemo1.py


# 变量和字符串
'''
1. encode和decode
2. python中如何避免中文是乱码
'''

# 经验一：在开头声明：
# -*- coding: utf-8 -*-

# 经验二：遇到字符（节）串，立刻转化为unicode，不要用str()，直接使用unicode()
# print(unicode_str.encode('utf-8'))

# 经验三：如果对文件操作，打开文件的时候，最好用codecs.open，替代open(这个后面会讲到，先放在这里)
# codecs.open('filename', encoding='utf8')

# 经验四：声明字符串直接加u，声明的字符串就是unicode编码的字符串
a = u"中"

a = '中'
print(type(a))  # <class 'str'>
# print(help(str))

print(len(a))
# b = a.decode()
# print(b)

b = a.encode('gbk')
print(type(b))  # <class 'bytes'>
