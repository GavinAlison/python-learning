#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 22:36
# @Author  : alison
# @File    : list02.py


# list
#  1. append与extend的区别
#  2. count用法
#  3. index()的用法

'''
append()和extend()的相同点：
1. 都是原地修改列表内容
2，没有返回值
不同点：
1. append()可添加数据等非iterable类型的元素, extend不行
2. append修改list的哈希地址，extend不变
'''
list1 = [1, 2, 3, 4, 5]
list1[len(list1):] = 'a'
print(list1)

c = list1.count(3)
i = list1.index(3)
print(c)
print(i)
