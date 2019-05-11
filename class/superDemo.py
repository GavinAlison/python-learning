#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 20:52
# @Author  : alison

'''
super(Girl, self).func
调用父类的方法和属性
'''
__metaclass__ = type


class Person:
    def __init__(self):
        self.height = 160

    def about(self, name):
        print('{} is about {}'.format(name, self.height))


class Girl(Person):
    def __init__(self):
        super(Girl, self).__init__()
        self.breast = 90

    def about(self, name):
        print('{} is a hot girl, she is about {}, and her breast is {}'.format(name, self.height, self.breast))
        super(Girl, self).about(name)


if __name__ == '__main__':
    alison = Girl()
    alison.about('alison')
