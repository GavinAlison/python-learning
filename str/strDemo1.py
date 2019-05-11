#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 20:49
# @Author  : alison
# @File    : strDemo1.py


# 变量和字符串
'''
1. 变量无类型，对象有类型
2. str和Int互转
3. 拼接字符串
4. str()与repr()区别


'''
# 变量无类型，对象有类型


# str和Int互转
a = 5
b = 'hello world'
# print(a + b)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
c = '123'
c = int(c)
a = str(a)

repr(a)
str(a)


# 转义
# 转义字符	描述
# \	(在行尾时) 续行符
# \	反斜杠符号
# \'	单引号
# \"	双引号
# \a	响铃
# \b	退格(Backspace)
# \e	转义
# \000	空
# \n	换行
# \v	纵向制表符
# \t	横向制表符
# \r	回车
# \f	换页
# \oyy	八进制数，yy代表的字符，例如：\o12代表换行
# \xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
# \other	其它的字符以普通格式输出
