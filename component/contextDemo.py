#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/20 23:07
# @Author  : alison


'''


定义：  上下文管理器
含有__enter__和__exit__的就是上下文管理器

'''


#  自定义上下文管理器


class ContextManagerDemo(object):
    def __init__(self):
        print('init')

    def __enter__(self):
        print('starting the manager')

    def __exit__(self, *args):
        print('exiting the manager')


with ContextManagerDemo():
    print('In the ContextManager')


# --------------------------------
class ContextManagerOpenDemo(object):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('starting the manager')
        self.open_file = open(self.filename, self.mode, encoding='utf-8')
        return self.open_file

    def __exit__(self, *args):
        self.open_file.close()
        print('exiting the manager')


with ContextManagerOpenDemo('iterDemo.py', 'r') as  reader:
    print('in the manager')
    for line in reader:
        print(line)
