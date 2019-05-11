#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/16 22:09
# @Author  : alison
# @File    : 6.py

# for ... in  list
# range(5)  list()
# while

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

print(list(range(5)))

sum1 = 0
for x in list(range(11)):
    sum1 = sum1 + x
print(sum1)


sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)