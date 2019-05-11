#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 22:36
# @Author  : alison
# @File    : list02.py


# list
#  1. 关键的方法： append、 count、 extend、index、 pop、remove、reversed、sort
#  2.


list1 = [1, 2, 3, 4, 5]
print('list1====', list1)
# list1==== [1, 2, 3, 4, 5]
list2 = ['q', 'a', 'z', 'w', 's']
list3 = list1.extend(list2)
print('list2====', list2)
# list2==== ['q', 'a', 'z', 'w', 's']
print('list3====', list3)
# list3==== None
print('list1====', list1)
# list1==== [1, 2, 3, 4, 5, 'q', 'a', 'z', 'w', 's']
print(dir(list))
print(list.extend.__doc__)
print(help(list.extend))


