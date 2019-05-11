#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 20:53
# @Author  : alison
# @File    : collectionsDemo.py


#  双向队列


import collections

# 创建双向队列
d = collections.deque()
# append(往右边添加一个元素)
d.append(1)
d.append(2)
d.append(3)
d.append(4)
print(d)
# appendleft（往左边添加一个元素）
d.appendleft(9)
print(d)
# deuqe([9,1,2,3,4])

# clear 清空队列
# d.clear()
# print(d)
# copy(浅拷贝)
new_d = d.copy()
print(new_d)
# count(返回指定元素的出现次数)
print(d.count(1))
# extend(从队列右边扩展一个列表的元素)
d.extend([6, 7, 8])
print(d)

# extendleft(从队列左边扩展一个列表的元素)
d.extendleft([0, 0, 0])
print(d)
# index（查找某个元素的索引位置）
print(d.index(0))
# #指定查找区间
print(d.index(0, 2, 8))
# insert（在指定位置插入元素）
d.insert(2, 's')
print(d)
# pop（获取最右边一个元素，并在队列中删除）
d.pop()
print(d)
# popleft（获取最左边一个元素，并在队列中删除）
d.popleft()
print(d)
# remove（删除指定元素）
d.remove('s')
print(d)
# reverse（队列反转）
d.reverse()
print(d)
print('-----------')
# rotate（把右边元素放到左边）
d.rotate(2)
print(d)
