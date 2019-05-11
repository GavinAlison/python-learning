#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 20:49
# @Author  : alison
# @File    : strDemo4.py

'''
1. 字符串格式化，常用的字符串方法
'''

# 字符串格式化输出


print("I like %s" % "python")

print("Suzhou is more than %d years. %s lives in here." % (2500, "qiwsir"))

# string.format()的格式化方法，其中{索引值}作为占位符，

s2 = "Suzhou is more than {0} years. {1} lives in here.".format(2500, "alison")

# 常用的字符串方法
dir(str)

"python".isalpha()  # 字符串全是字母，应该返回True
'python'.isalpha()

# split
# 作用是将字符串根据某个分割符进行分割
a = "I LOVE PYTHON"
a.split(" ")
a.split(" ")

b = "www.itdiffer.com"
b.split(".")
b.split('.')

# S.strip() 去掉字符串的左右空格
# S.lstrip() 去掉字符串的左边空格
# S.rstrip() 去掉字符串的右边空格
# 去掉字符串两头的空格

b = " hello "  # 两边有空格
b.strip()
# 特别注意，原来的值没有变化，而是新返回了一个结果。

b.strip()
b.lstrip()
b.rsplit()

# 字符大小写的转换
# S.upper() #S中的字母大写
# S.lower() #S中的字母小写
# S.capitalize() #首字母大写
# S.isupper() #S中的字母是否全是大写
# S.islower() #S中的字母是否全是小写
# S.istitle() #S中字符串中所有的单词拼写首字母是否为大写，且其他字母为小写

# print(dir(str))

a = 'alison'
a.upper()
a.lower()
a.capitalize()
b = 'Alison, alison'
b.istitle() # False
a.isupper()
a.islower()


# join拼接字符串
b = 'www.github.com'
print('b=',b)
c = b.split('.')
print('.'.join(c))
