#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 21:32
# @Author  : alison
# @File    : sysDemo.py


'''
This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.
'''

'''
sys
    1. argv
    2. path
    3. stdin/stdout/stderr
    4. exit

'''

import sys

print('the file name : %s' % sys.argv[0])
print('the number of argument %d ' % len(sys.argv))
print('the argument is : %s' % str(sys.argv))

for i in range(10):
    if i == 5:
        sys.exit()
    else:
        print(i)

print('sys.path===' + str(sys.path))
