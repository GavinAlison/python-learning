#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 23:16
# @Author  : alison
# @File    : contextLibDemo.py


from contextlib import contextmanager


@contextmanager
def foo():
    print('before yeild')
    yield 'contentManager demo'
    print('after yeild')


with foo()  as dd:
    print('the world is : %s' % dd)
