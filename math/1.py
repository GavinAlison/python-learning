#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 22:47
# @Author  : alison
# @File    : 1.py


# 使用math模块

import math

# print(math.pi)
# dir(module)是一个非常有用的指令，可以通过它查看任何模块中所包含的工具

# print(dir(math))
# 展示了math模块中的pow函数的使用方法和相关说明
#  help(math, pow)

# print(4 ** 3)
# print(math.pow(4, 3))
#
# print(math.sqrt(9))
# print(math.floor(3.92))
# print(math.fabs(-2))
# print(math.fmod(7, 6))
# print(7 % 6)

# 几个常见函数
# abs(num)
# 四舍五入
# round(num)
print(round(1.234))
print(round(1.234, 2))


# 运算优先级
# 一套新规范了，只需要符合数学中的即可。
#
# 运算符	描述
# lambda	Lambda表达式
# or	布尔“或”
# and	布尔“与”
# not x	布尔“非”
# in，not in	成员测试
# is，is not	同一性测试
# <，<=，>，>=，!=，==	比较
# \	按位或
# ^	按位异或
# &	按位与
# <<，>>	移位
# +，-	加法与减法
# *，/，%	乘法、除法与取余
# +x，-x	正负号
# ~x	按位翻转
# **	指数
# x.attribute	属性参考
# x[index]	下标
# x[index:index]	寻址段
# f(arguments...)	函数调用
# (experession,...)	绑定或元组显示
# [expression,...]	列表显示
# {key:datum,...}	字典显示
# 'expression,...'	字符串转换