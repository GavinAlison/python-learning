#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 9:20
# @Author  : alison
# @File    : 16.py

#  python多继承（新式类）一
#  实际上打印出来的信息是 A foo，这就说明了调用的是A中的方法。其实在python2.2之后，多继承中基类的寻找顺序是一种广度优先算法，称之为C3的算法（后续博客我会简单介绍下C3算法）。而python2.2之前，使用的是深度优先算法来寻找基类方法。在类C的继承关系中，按照广度优先算法，则会先找到靠近C的基类A，在A中找到foo方法之后，就直接返回了，因此即使后面的基类B中也有foo方法，但是这里不会引用它。
class A(object):
    def __init__(self):
        pass

    def foo(self):
        print
        print('A foo')


class B(object):
    def __init__(self):
        pass

    def foo(self):
        print
        print('B foo')


class C(A, B):
    def __init__(self):
        pass


testc = C()

testc.foo()
