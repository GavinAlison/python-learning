#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/17 21:15
# @Author  : alison
# @File    : 10.py

import requests

 #get请求方法
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
#打印get请求的状态码
print(r.status_code)
200
#查看请求的数据类型，可以看到是json格式，utf-8编码
print(r.headers['content-type'])
#'application/json; charset=utf8'
print(r.encoding)
#'utf-8'
#打印请求到的内容
print(r.text)
#u'{"type":"User"...'
#输出json格式数据
print(r.json())
#{u'private_gists': 419, u'total_private_repos': 77, ...}