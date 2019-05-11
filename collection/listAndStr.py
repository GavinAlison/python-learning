#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 22:36
# @Author  : alison
# @File    : list02.py


# list与str的区别
# 相同点
# 所谓序列类型的数据，就是说它的每一个元素都可以通过指定一个编号，行话叫做“偏移量”的方式得到，而要想一次得到多个元素，可以使用切片。偏移量从0开始，总元素数减1结束

# 区别
# ist和str的最大区别是：list是可以改变的，str不可变。这个怎么理解呢？


# 多维list
# 这个也应该算是两者的区别了，虽然有点牵强。在str中，里面的每个元素只能是字符，在list中，元素可以是任何类型的数据。前面见的多是数字或者字符，其实还可以这样：

# list和str转化
# str.split()
# 这个内置函数实现的是将str转化为list。其中str=""是分隔符。
# "[sep]".join(list)


welcome_str = "Welcome you"
welcome_str[0]
# 'W'
welcome_str[1]
# 'e'
welcome_str[len(welcome_str) - 1]
# 'u'
welcome_str[:4]
# 'Welc'
a = "python"
a * 3
# 'pythonpythonpython'

git_list = ["qiwsir", "github", "io"]
git_list[0]
# 'qiwsir'
git_list[len(git_list) - 1]
# 'io'
git_list[0:2]
# ['qiwsir', 'github']
b = ['qiwsir']
b * 7
# ['qiwsir', 'qiwsir', 'qiwsir', 'qiwsir', 'qiwsir', 'qiwsir', 'qiwsir']

first = "hello,world"
welcome_str
'Welcome you'
first + "," + welcome_str  # 用+号连接str
'hello,world,Welcome you'
welcome_str  # 原来的str没有受到影响，即上面的+号连接后重新生成了一个字符串
'Welcome you'
first
'hello,world'

language = ['python']
git_list
# ['qiwsir', 'github', 'io']
language + git_list  # 用+号连接list，得到一个新的list
# ['python', 'qiwsir', 'github', 'io']
git_list
# ['qiwsir', 'github', 'io']
language
# ['python']

len(welcome_str)  # 得到字符数
# 11
len(git_list)  # 得到元素数
# 3
git_list
['qiwsir', 'github', 'io']

git_list.append("python")
git_list
['qiwsir', 'github', 'io', 'python']

git_list[1]
# 'github'
git_list[1] = 'github.com'
git_list
# ['qiwsir', 'github.com', 'io', 'python']

git_list.insert(1, "algorithm")
git_list
# ['qiwsir', 'algorithm', 'github.com', 'io', 'python']

git_list.pop()
# 'python'

del git_list[1]
git_list
# ['qiwsir', 'github.com', 'io']


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[0][1]

# list和str转化

line = 'hello. i am alison . welcome you.'
line_list = line.split('.')
# 以英文的句点为分隔符，得到list
print(line_list)
line_list = line.split('.', 1)
# 这个1,就是表达了上文中的：If maxsplit is given, at most maxsplit splits are done.
print(line_list)
name = 'alison gavin'
print(name.split(' '))
# 也有可能用空格来做为分隔符
print(name.split())
# 也有可能默认空格来做为分隔符
s = 'i am alison, writing\npython\tbook on line '
print(s)
print(s.split())
# 用split(),但是括号中不输入任何参数
# 这个字符串中有空格，逗号，换行\n，tab缩进\t 符号

lst = s.split()
str = "".join(lst)
# 将list中的元素连接起来，但是没有连接符，表示一个一个紧邻着
print(str)
str = '.'.join(lst)
# 以英文的句点做为连接分隔符
print(str)
str = ' '.join(lst)
# 以空格做为连接的分隔符
print(str)