#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/16 22:14
# @Author  : alison
# @File    : 7.py

# dict 字典   [key: value1, lkey2: value2]
# key 不可变性，查找和插入的速度极快，占用大量的内存（相对较与list）
# set key集合，key不能重复, 无序和无重复元素的集合
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
'Thomas' in d
# False
# 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
d.get('Thomas', -1)
#-1


##################
s = set([1, 2, 3])


# str, int是不变对象，而list是可变对象

