#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 20:50
# @Author  : alison
# @File    : bsDemo.py

# >详见:https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html

from bs4 import BeautifulSoup as bs

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = bs(html_doc, 'lxml')
print(soup.prettify())

print(soup.title)
# <title>The Dormouse's story</title>
print(soup.title.name)
# u'title'

print(soup.title.string)
# The Dormouse's story

print(soup.title.parent.name)
# u'head'

print(soup.p)
# <p class="title"><b>The Dormouse's story</b></p>
print(soup.p['class'])
# ['title']

print(soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print(soup.find_all('a'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print(soup.find_all(id='link3'))
# [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
print(type(soup.find_all(id='link3')))
# <class 'bs4.element.ResultSet'>

for link in soup.find_all('a'):
    print(link.get('href'))
    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie
print(soup.get_text())

soup = bs('<b class="boldest">Extremely bold</b>', 'lxml')
tag = soup.b
print(type(tag))
# <class 'bs4.element.Tag'>
print(tag.name)
# u'b'
print(tag['class'])
# ['boldest']
print(tag.attrs)
# {'class': ['boldest']}

# 多值属性
css_soup = bs('<p class="body strikeout"></p>', 'lxml')
print(css_soup.p['class'])
# ['body', 'strikeout']
css_soup = bs('<p class="body"></p>', 'lxml')
print(css_soup.p['class'])
# ['body']


id_soup = bs('<p id="my id"></p>', 'lxml')
print(id_soup.p['id'])
# u'my id'

rel_soup = bs('<p>Back to the <a rel="index">homepage</a></p>', 'lxml')
print(rel_soup.a['rel'])
# ['index']
rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)
# <p>Back to the <a rel="index contents">homepage</a></p>
# 如果转换的文档是XML格式,那么tag中不包含多值属性
xml_soup = bs('<p class="body strikeout"></p>', 'xml')
print(xml_soup.p['class'])

# 字符串
soup = bs('<b class="boldest">Extremely bold</b>', 'lxml')
print(soup.string)
# Extremely bold
print(type(soup.string))
# <class 'bs4.element.NavigableString'>
print(soup.string.replace_with('haha'))
print(soup)



# find()
# find( name , attrs , recursive , text , **kwargs )
html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = bs(html_doc, 'lxml')
# find_all() tag, name
#  str
soup.find_all('b')
# 正则表达式
import re
for tag in soup.find_all(re.compile('b')):
    print(tag.name)
for tag in soup.find_all(re.compile("t")):
    print(tag.name)
print('------------')
print(soup.find_all(["a", "b"]))
# True
for tag in soup.find_all(True):
    print(tag.name)
# 方法
def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
s = soup.find_all(has_class_but_no_id)
print(s)

from bs4 import NavigableString
def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))

for tag in soup.find_all(surrounded_by_strings):
    print(tag.name)
# find_all( name , attrs , recursive , text , **kwargs )
# find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
# name: name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉.
# keyword : 如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索,如果包含一个名字为 id 的参数,
# 搜索指定名字的属性时可以使用的参数值包括 字符串 , 正则表达式 , 列表, True .

# 按CSS搜索
print(soup.find_all("a", class_="sister"))


# .这里有几个例子:
soup.find_all("title")
# [<title>The Dormouse's story</title>]

soup.find_all("p", "title")
# [<p class="title"><b>The Dormouse's story</b></p>]

soup.find_all("a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

soup.find_all(id="link2")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

import re
soup.find(text=re.compile("sisters"))
# u'Once upon a time there were three little sisters; and their names were\n'

