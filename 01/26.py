#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 9:20
# @Author  : alison
# @File    : 16.py

# type()

def foo():
    r = open('1.txt')
    if r == (-1):
        return (-1)
    # do something
    return r


def bar():
    r = foo()
    if r == (-1):
        print('Error')
    else:
        pass


# try:
#     print('try....')
#     r = 10 / 0
#     print('result: ', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally....')
# print('end')

# try:
#     print('try....')
#     r = 10 / int('a')
#     print('result:', r)
# except ValueError as e:
#     print(e)
# except ZeroDivisionError as e:
#     print(e)
# finally:
#     print('finally....')
# print('end')

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
