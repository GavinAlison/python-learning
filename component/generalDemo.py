#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 22:30
# @Author  : alison

'''
生成器,  通过生成器解析式得到的生成器。
    定义： 含yeild的语句就是  生成器
    方法： next(), send()

'''


def g():
    yield 0
    yield 1
    yield 2


# gene = g()
# print(dir(gene))
# print(next(gene))
# print(next(gene))
# print(next(gene))


def t_return(n):
    print('you take me.')
    while n > 0:
        print('before return')
        return n
        print('after return')


def y_yield(n):
    print('you tabled me.')
    while n > 0:
        print('before yield')
        yield n
        n -= 1
        print('after yield')

yy = y_yield(5)
print(next(yy))
print(next(yy))
print(next(yy))
