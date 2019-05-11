#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 23:15
# @Author  : alison
# @File    : list01.py

# 变量没有类型，对象有类型

# 用方括号表示一个list，[ ]

'''
a = []  # 定义了一个变量a，它是list类型，并且是空的。
type(a)
# <type 'list'>   #用内置函数type()查看变量a的类型，为list
bool(a)  # 用内置函数bool()看看list类型的变量a的布尔值，因为是空的，所以为False
# False
print(a)
# []  #打印list类型的变量a
'''


a = ['2', 3, 'alison.github.com']
print(a)
print(type(a))

# ========2============
# java中的list， 实现为不定长数组，指定泛型,list中的元素类型为指定的，都是一样的
# 但是python中的list，尽管跟java中的数组有类似的地方——都是[]包裹的——list中的元素是任意类型的，可以是int,str，甚至还可以是list
# 等效于 java: list<Object> = python: list
