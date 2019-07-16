#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 22:22
# @Author  : alison
# @File    : 4.py

'''
1. re.match(pattern, str) ---
2. re.search(pattern, str) -- match(endpos, lastgroup, lastindex, pos)
3. re.search(pattern, str).group() --
4. re.split(pattern, str) -- class list ['', '', '']
5. re.findall(pattern, str) -- class list ['', '', '']
6. re.finditer(pattern, str) -- callable_iterator
6. re.sub(patter, newstr, str) -- str, 正则替换


'''

import re

pattern = re.compile(r'world')
match = re.search(pattern, 'hello world')
# <re.Match object; span=(6, 11), match='world'>
## 可以匹配到，是匹配整个字符串
if match:
    print(match.group())

match1 = re.match(pattern, 'hello world')
# None
## 匹配不到数据, match是从开头开始匹配的
try:
    if match1:
        print(match1.group())
except Exception as e:
    print('error')

print('--------------re.split(pattern, string[, maxsplit])-----------')
# split
pattern = re.compile(r'\d+')
print(re.split(pattern, 'onetwo2three3four4'))
# <class 'list'>: ['onetwo', 'three', 'four', '']
##['onetwo', 'three', 'four', '']

print('-----------findall------------')
pattern = re.compile(r'\d+')
items = re.findall(pattern, 'onetwo2three3four4')
# <class 'list'>: ['2', '3', '4']
print(items)
for item in items:
    print(item)

print('------------re.finditer-------------')
pattern = re.compile(r'\d+')
re.finditer(pattern, 'onetwo2three3four4')
# <callable_iterator object at 0x03A1CD70>
for m in re.finditer(pattern, 'onetwo2three3four4'):
    print(m.group())

print('---------------sub()')
pattern = re.compile(r'(\s+)')
text = 'JGood is a handsome boy, he is cool, clever, and so on...'

print(re.sub(pattern, '-', text))
# JGood-is-a-handsome-boy,-he-is-cool,-clever,-and-so-on...

def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()


print(re.sub(pattern, lambda m: '[' + m.group(0) + ']', text))
# JGood[ ]is[ ]a[ ]handsome[ ]boy,[ ]he[ ]is[ ]cool,[ ]clever,[ ]and[ ]so[ ]on...

print('-----------subn(pattern, repl, string, count=0, flags= 0)')
print(re.subn('[1-2]', 'A', '123456abcdef'))
print(re.sub('g.t', 'have', 'I get A, I got B, I gut C'))
print(re.subn("g.t", "have", 'I get A,  I got B ,I gut C'))

a = re.findall(r"a(\d+?)", 'a23b')
print(a)
b = re.findall(r"a(\d+)", 'a23b')
print(b)
'''执行结果：
['2']
['23']'''

a = re.match('<(.*)>', '<H1>title<H1>').group()
print(a)
b = re.match('<(.*?)>', '<H1>title<H1>').group()
print(b)
'''执行结果：
<H1>title<H1>
<H1>'''

a = re.findall(r"a(\d+)b", 'a3333b')
print(a)
b = re.findall(r"a(\d+?)b", 'a3333b')
print(b)
'''
执行结果如下：
['3333']
['3333']
这里需要注意的是如果前后均有限定条件的时候，就不存在什么贪婪模式了，非匹配模式失效。
'''

print(re.split('a', '1A1a2A3', re.I))  # 输出结果并未能区分大小写
'''这是因为re.split(pattern，string，maxsplit,flags)默认是四个参数，当我们传入的三个参数的时候，系统会默认re.I是第三个参数，所以就没起作用。如果想让这里的re.I起作用，写成flags=re.I即可。 '''

##1、匹配电话号码
p = re.compile(r'\d{3}-\d{6}')
print(p.findall('010-628888'))

# 2、匹配IP
re.search(r"(([01]?\d?\d|2[0-4]\d|25[0-5])\.){3}([01]?\d?\d|2[0-4]\d|25[0-5]\.)", "192.168.1.1")
