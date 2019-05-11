#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 9:20
# @Author  : alison
# @File    : 16.py

# raise except
class FooErr(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooErr('invalid value %s' % s)
    return 10 / s


foo('0')
