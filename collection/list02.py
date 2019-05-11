#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 22:36
# @Author  : alison
# @File    : list02.py


# list
#  1. 方法： len()、[position]取值、append(val)、pop()、insert(position, val)
#  2. 反转 list[::-1]   或者 reversed(list)
#  3. 运算方法：
#       3.1 + 连接序列,
#       3.2 list * num 重复序列，
#       3.3 element in list 判断元素是否在序列中
#       3.4 max(list)  和   min(list)
#       3.5 cmp(list1, list2)  比较两个序列
#       3.6 list.append(element)
# tuple
# 定义: (1,2,)
cls = ['a', 'b', 'c']
print(dir(list))
print(cls)
print(cls[0])
print(cls[-1])
print(len(cls))
print(cls.append('dd'))
print(cls)
print(cls.pop())
print(cls)
# insert 在指定位置插入指定值，如果指定位置有值，将该值后移
print(cls.insert(-1, 'haha'))
print(cls)
print(cls[-1])
print(cls.insert(0, 's'))
print(cls)

print('----------')
a = ['123', '123', 'asd', 123]
print(a.count('123'))

print('-----------')
lang = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lang1 = lang[::-1]
print(lang1)
lang2 = reversed(lang)
print(lang2)
print(list(lang2))

