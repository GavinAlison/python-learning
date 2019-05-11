#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 9:20
# @Author  : alison
# @File    : 16.py

# extends mulit  override overload
import sys

type(123)

isinstance(123, int)

isinstance([1, 2, 3], (list, tuple))

print(dir(sys))

print(dir('123'))

hasattr('123', '__len__')

getattr('123', '__len__')

#  setattr(o, attribute, value)


# 实例属性属于各个实例所有，互不干扰；
#
# 类属性属于类所有，所有实例共享一个属性；
#
# 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。
