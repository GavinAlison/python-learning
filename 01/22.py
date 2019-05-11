#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 9:20
# @Author  : alison
# @File    : 16.py

#  使用__slots__

from types import MethodType


class Student(object):
    pass


s = Student()
s.name = 'alison'
print(s.name)


def set_age(self, age):
    self.age = age


# 给实例绑定方法
s.set_age = MethodType(set_age, s)
s.set_age(22)

s1 = Student()
# AttributeError: 'Student' object has no attribute 'set_age'
# s1.set_age(11)


print('====================')


#  给类绑定方法

def set_haha(self, haha):
    self.haha = haha


Student.set_haha = set_haha

s1.set_haha('haha')
print(s1.haha)


class Person(object):
    # 定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
    __slots__ = ('name', 'age')


p = Person()
p.name = 'alison'
# AttributeError: 'Person' object has no attribute 'address'
# p.address = 'adress'
# 用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：


