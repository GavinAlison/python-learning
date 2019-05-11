#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/13 21:58
# @Author  : alison
# @File    : defDemo1.py


'''
函数
定义:
    1. def function_name(x...):
        pass
    2. 特殊函数map, reduce, filter, lambda，[], zip


'''


# x,y并没有严格规定其所引用的对象类型
def add(x, y):
    return x + y


# x+y的意义完全取决于对象的类型。在python中，将这种依赖关系，称之为多态
# python中为对象编写接口，而不是为数据类型

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multi(x, y):
    return x * y


def div(x, y):
    return x / y
