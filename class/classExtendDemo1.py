#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 20:34
# @Author  : alison


'''
1. class类
    定义：  class class_name():
    类型的初始化函数 __init__
    类的属性， 方法/函数, 类和实例,  self的作用,
    类属性和实例属性， 数据流转，
    命名空间  namespace
        built-in namespace
        module: global namespace
        function: local namespace
    作用域

2.  类的多重继承
        class A(B, C)
    多重继承的顺序
        使用的广度优先算法
'''


class K1():
    def foo(self):
        print('k1 foo')


class K2():
    def foo(self):
        print('k2  foo')

    def bar(self):
        print('k2 bar')


class J1(K1, K2):
    pass


class J2(K1, K2):
    def bar(self):
        print('J2 bar')


class C(J1, J2):
    pass


if __name__ == '__main__':
    print(C.__mro__)
    m = C()
    m.foo()
    m.bar()
