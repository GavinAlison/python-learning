#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/10 20:49
# @Author  : alison
# @File    : strDemo2.py

'''
1. 内建函数，
2. 原始字符串，
'''
# build-in functions
# 所谓内建函数，就是能够在python中直接调用，不需要做其它的操作
'''
|abs() | divmod() | input()| open()| staticmethod()|
|all() | enumerate() | int() | ord() | str()|
|any() | eval() | isinstance()| pow()| sum()|
|basestring() | execfile() | issubclass() | print() | super()|
|bin() | file() | iter()| property()| tuple()|
|bool() | filter() | len() | range() | type()|
|bytearray() | float()| list() | raw_input()| unichr()|
|callable() | format() | locals() | reduce() | unicode()|
|chr() | frozenset() | long() | reload() | vars()|
|classmethod()| getattr()| map() | repr() | xrange()|
|cmp() | globals()| max()| reversed()| zip()|
|compile() |hasattr() | memoryview()| round() | import()|
|complex() |hash() | min()| set() | apply()|
|delattr() |help()| next()| setattr()| buffer()|
|dict() | hex() |object() |slice() | coerce()|
|dir() | id() |oct() |sorted() |intern()|

'''
# abs(12)
divmod(10, 3)
# input()
# open()
# staticmethod()
# all()
# enumerate()
# int()
# ord()
# str()
# any()
# eval()
# isinstance()
# pow(2,2)
# sum(2,3,4)
# basestring()
# execfile()
# issubclass()
print()
# super()
# bin()
# file()
# iter()
# property()
# tuple()
# bool()
# filter()
# len()
# range()
# type()
# bytearray()
# float()
# list()
# raw_input()
# unichr()
# callable()
# format()
# locals()
# reduce()
# unicode()
# chr()
# frozenset()
# long()
# reload()
# vars()
# classmethod()
# getattr()
# map()
# repr()
# xrange()
# cmp()
# globals()
# max()
# reversed()
# zip()
# compile()
# hasattr()
# memoryview()
# round()
# import()
# complex()
# hash()
# min()
# set()
# apply()
# delattr()
# help()
# next()
# setattr()
# buffer()
# dict()
# hex()
# object()
# slice()
# coerce()
dir()
# id()
# oct()
# sorted()
# intern()

dos = 'c:\news'
print(dos)
# 1
dos = 'c:\\news'
print(dos)
# 2
dos = r'c:\news'
print(dos)
# 由r开头引起的字符串，就是原始字符串，在里面放任何字符都表示该字符的原始含义。
