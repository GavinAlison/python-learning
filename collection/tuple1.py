#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 23:30
# @Author  : alison
# @File    : tuple1.py

'''
1. tuple定义： (,,,)
2. 字符串的格式化输出 %(,)
3. 特点, immutable不可变性
4. 取值， 索引和切片[index:]
5. tuple与list互转
6. 用处, 遍历快，格式化
'''
# 元组
# 定义
# 元组是用圆括号括起来的，其中的元素之间用逗号隔开。（都是英文半角）
# 变量引用str
s = 'asd'
print(s)
# 如果这样写，就会是...
t = 123, 'asd', ['a', 's']
print(t)

# 字符串的格式化输出
print('I love %s, and I am %s' % ('haha', 'hehe'))

# 特点
# tuple是一种序列类型的数据，这点上跟list/str类似。它的特点就是其中的元素不能更改，这点上跟list不同，倒是跟str类似；它的元素又可以是任何类型的数据，这点上跟list相同，但不同于str。
t = 1, "23", [123, "abc"], ("python", "learn")  # 元素多样性，近list
# t[0] = 8  # 不能原地修改，近str  报错
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# t.append("no")  ##报错
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'tuple' object has no attribute 'append'


# 索引和切片
print(t)
print(t[2])
print(t[1:])
print(t[2][0])
print(t[3][1])

# 关于序列的基本操作在tuple上的表现，就不一一展示了。看官可以去试试。

# 注意：如果一个元组中只有一个元素的时候，应该在该元素后面加一个半角的英文逗号。
# 如果要想看一个对象是什么类型，可以使用type()函数，然后就返回该对象的类型。

a = (3)
print(type(a))
a = (3,)
print(type(a))

# 所有在list中可以修改list的方法，在tuple中，都失效。


# tuple与list互转
print(t)
tlist = list(t)
print(tlist)
t_tuple = tuple(tlist)
print(t_tuple)

# tuple用在哪里？
# 1. Tuple 比 list 操作速度快。如果您定义了一个值的常量集，并且唯一要用它做的是不断地遍历它，请使用 tuple 代替 list。
# 2. 如果对不需要修改的数据进行 “写保护”，可以使代码更安全。使用 tuple 而不是 list 如同拥有一个隐含的 assert 语句，说明这一数据是常量。如果必须要改变这些值，则需要执行 tuple 到 list 的转换 (需要使用一个特殊的函数)。
# 3. Tuples 可以在 dictionary（字典，后面要讲述） 中被用做 key，但是 list 不行。Dictionary key 必须是不可变的。Tuple 本身是不可改变的，但是如果您有一个 list 的 tuple，那就认为是可变的了，用做 dictionary key 就是不安全的。只有字符串、整数或其它对 dictionary 安全的 tuple 才可以用作 dictionary key。
# 4. Tuples 可以用在字符串格式化中。
