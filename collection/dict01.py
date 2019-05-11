#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/11 17:54
# @Author  : alison
# @File    : dict01.py

# 1. dict
#   定义， 增加，修改，删除， 取值， 设值
#

# 定义
ad = {}
ad['name'] = 'alison'
name = (['first', 'google'], ['second', 'Yahoo'])
website = dict(name)
print(website)
ad = dict(name='alison', sex=1)
print(ad)

website = {}.fromkeys(('third', 'forth'), 'facebook')
print(website)
# 在字典中的“键”，必须是不可变的数据类型；“值”可以是任意数据类型。

# len(d)，返回字典(d)中的键值对的数量
# d[key]，返回字典(d)中的键(key)的值
# d[key]=value，将值(value)赋给字典(d)中的键(key)
# del d[key]，删除字典(d)的键(key)项（将该键值对删除）
# key in d，检查字典(d)中是否含有键为key的项

# 字符串格式化输出

temp = "<html><head><title>%(lang)s<title><body><p>My name is %(name)s.</p></body></head></html>"
my = {"name": "qiwsir", "lang": "python"}
print(temp % my)



