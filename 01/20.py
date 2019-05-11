#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 9:20
# @Author  : alison
# @File    : 16.py

# class

class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def print_field(self):
        print('%s %s' % (self.__name, self.__age))


bart = Student('alison', 22)
# bart1 = Student()
bart.print_field()
# print(bart.name)  # AttributeError: 'Student' object has no attribute 'name'
# print(bart.age)  # AttributeError: 'age' object has no attribute 'name'
# print(bart1)



