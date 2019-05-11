#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 9:20
# @Author  : alison
# @File    : 16.py

# 匿名函数
print(list(map(lambda x: x * x, list(range(1, 10)))))


# 装饰器
def now():
    print('2018-12-23')


f = now
f()
print(now.__name__)
print(f.__name__)


def log(func):
    def wrapper(*args, **kw):
        print('call ', func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now1():
    print('2018-12-23')


now1()

print('=============')


# @的用法
# 在Python的函数中偶尔会看到函数定义的上一行有@functionName的修饰，当解释器读到@的这样的修饰符之后，会先解析@后的内容，直接就把@下一行的函数或者类作为@后边的函数的参数，然后将返回值赋值给下一行修饰的函数对象。
def funcA(a):
    print('function a')


def funcB(b):
    print(b(4))
    print('function b')


@funcA
@funcB
def funcC(c):
    print('function c')
    return c * 2
