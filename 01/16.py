#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 9:20
# @Author  : alison
# @File    : 16.py

# 闭包， 返回函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f)
# <function lazy_sum.<locals>.sum at 0x01B8CED0>
print(f())
print(calc_sum(1, 3, 5, 7, 9))

