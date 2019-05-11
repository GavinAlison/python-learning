#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 17:54
# @Author  : alison

import copy

# 1. dict
#  copy浅拷贝与深拷贝
#  clear :  Remove all items from D.
#  list,get('key')    list['key']
#  list.pop('key')
#  list.popitem()随机删除一对
a = 5
b = a
print(id(a))
print(id(b))

ad = {'name': 'alison', 'lang': 'python'}
bd = ad
print(bd)
print(id(ad))
print(id(bd))
bds = ad.copy()
print(id(bds))
# 在编程语言中，把实现上面那种拷贝的方式称之为“浅拷贝”。
# 用copy.deepcopy()深拷贝了一个新的副本，看这个函数的名字就知道是深拷贝(deepcopy)
print('-----------')
x = {'lang': ['python', 'java'], 'name': 'alison'}
z = copy.deepcopy(x)
print(id(x['lang']))
print(id(z['lang']))

a = {'name': 'alison'}
a.clear()
print(a)

print(x.get('lang'))
# dict.get()就是要得到字典中某个键的值，不过，它不是那么“严厉”罢了。因为类似获得字典中键的值得方法，上节已经有过，如d['lang']就能得到对应的值"python"，可是，如果要获取的键不存在，如：
d = {}
print(d.get("name"))
# None

# d["name"]
# Traceback(most recent call last):
# File "<stdin>", line 1, in < module > KeyError: 'name'
print('-----------')
dd = {'lang': 'python', 'web': 'www.itdiffer.com', 'name': 'alison'}
dd_iter = dd.items()
print(dd_iter)
dd_name = dd.pop('name')
print(dd_name)
