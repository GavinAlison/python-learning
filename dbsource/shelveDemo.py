#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 10:36
# @Author  : alison
# @File    : shelveDemo.py


import shelve
import datetime

'''
shelve 也可以序列化Python所有数据类型，而且可以多次序列化
shelve模块通过key-value方式持久化
'''
f = shelve.open('.//res//shelve_text')
info = {'a': 'A', 'b': 'B', 'c': 'C'}
list = ['qwe', 'asd', 'zxc']
date = datetime.datetime.now()
'''sequence'''
f['info'] = info
f['list'] = list
f['date'] = date
f.close()
'''
输出结果：会生成几个文件
'''
# 反序列化,通过get(key)来获取数据
f = shelve.open('.//res//shelve_text')
print(f.get('date'))
