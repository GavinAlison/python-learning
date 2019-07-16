#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/19 21:53
# @Author  : alison
# @File    : 3.py

__author__ = 'CQC'
# -*- coding: utf-8 -*-

'''
1. re.compile(r'str'|regex)
2. re.match(pattern, str)
3. re.match(pattern, str).group()
'''


# 导入re模块
import re

# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
pattern = re.compile(r'hello')

# 使用re.match匹配文本，获得匹配结果，无法匹配时将返回None, 从开头匹配
result1 = re.match(pattern, 'hello')
result2 = re.match(pattern, 'helloo CQC!')
result3 = re.match(pattern, 'helo CQC!')
result4 = re.match(pattern, 'hello CQC!')

# 如果1匹配成功
if result1:
    # 使用Match获得分组信息
    print(result1.group())
else:
    print('1匹配失败！')

# 如果2匹配成功
if result2:
    # 使用Match获得分组信息
    print(result2.group())
else:
    print('2匹配失败！')

# 如果3匹配成功
if result3:
    # 使用Match获得分组信息
    print(result3.group())
else:
    print('3匹配失败！')

# 如果4匹配成功
if result4:
    # 使用Match获得分组信息
    print(result4.group())
else:
    print('4匹配失败！')

print('-----------------')
#####
m = re.match(r'(\w+)(\W+)(?P<sign>.*)', 'hello world!')

print('m.string', m.string)
print('m.re', m.re)
print('m.pos ', m.pos)
print('m.endpos ', m.endpos)
print('m.lastindex ', m.lastindex)
print('m.lastgroup ', m.lastgroup)
print('m.group() ', m.group())
print('m.group(1, 2) ', m.group(1, 2))
print('m.groups() ', m.groups())
print('m.groupdict() ', m.groupdict())
print('m.start(2) ', m.start(2))
print('m.end(2) ', m.end(2))
print('m.span(2) ', m.span(2))
print(r'm.expand(r"\g \g\g ") ', m.expand(r'\2 \1\3'))
