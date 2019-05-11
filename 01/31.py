#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 9:20
# @Author  : alison
# @File    : 16.py

#  fork


import os

print('process (%s) start' % os.getpid())
# Only works on Unix/Linux/Mac:
# windows:AttributeError: module 'os' has no attribute 'fork'
pid = os.fork()
if pid == 0:
    print('i am child process (%s) and my parent is %s' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s)' % (os.getpid(), pid))
