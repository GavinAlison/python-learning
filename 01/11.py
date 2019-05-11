#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 22:37
# @Author  : alison
# @File    : 11.py

'''
异常的应用
try....except...finally...else
except种类:
常见的：
AttributeError 不存在属性
IoError  输入署出异常
ImportError 无法引入模块或包--一般路劲问题，或者模块名称
IndentationError  语法异常--SynataxError 子类，一般代码缩进异常
KeyError   字典中不存在关键字
KeyboardInterrupt Ctrl+C被按下
SyntaxError  语法错误
TypeError  传入对象类型与要求不符
UnboundLocalError 变量作用域问题
ValueError 传入不期望值
'''


def some_function():
    return -1;


def foo():
    r = some_function()
    if r == (-1):
        return -1
    pass
    return r


def bar():
    r = foo()
    if r == (-1):
        print('error')
    else:
        pass


try:
    print('try....')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except: ', e)
finally:
    print('finally....')
print('end')

print('------------')

try:
    r = 10 / int('a')
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
finally:
    print('finally....')
print('end')

print('-------------')
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

print('--------------')
x = 9


def test():
    print(x)


test()
print('----------but')
y = 9


def test1():
    print(y)
    y = 1  # python从上到下解释，会把y当做局部变量，然而上边print要打印未声明的局部变量，报错


try:
    test1()
except Exception as e:
    pass
print('------update')
z = 10


def test2():
    global z
    print(z)
    z = 11


test2()


class MyException(Exception):
    def __init__(self, name):
        self.msg = name

    def __str__(self):
        return self.msg  # 可以不重写，继承基类
try:
    flag = False
    if flag:
        pass
    else:
        raise MyException('your exception')
except MyException as e:
    print(e)