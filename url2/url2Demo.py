#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 20:24
# @Author  : alison
# @File    : url2Demo.py
# python 3.7


import urllib.request, urllib
from urllib.request import URLError

basic_url = 'https://www.cnblogs.com/billyzh/p/5819957.html'
# 由str 转换成byte
"".encode('utf-8')


# 获取URLs
# get_url_1
def get_url():
    response = urllib.request.urlopen('https://www.cnblogs.com/billyzh/p/5819957.html')
    html = response.read().decode('utf-8')
    print(html)


# get_url_2
def get_url_2():
    request = urllib.request.Request('https://www.cnblogs.com/billyzh/p/5819957.html')
    response = urllib.request.urlopen(request)
    html = response.read().decode('utf-8')
    print(html)


# url_info
def url_info():
    request = urllib.request.Request('https://www.cnblogs.com/billyzh/p/5819957.html')
    response = urllib.request.urlopen(request)
    info = response.info()
    url = response.geturl()
    print(info)
    print('---------url---------')
    print(url)
    html = response.read().decode('utf-8')
    # print(html)


# Data  -post
def data_post():
    url = 'http://www.someserver.com/cgi-bin/register.cgi'
    values = {}
    values['name'] = 'Alison'
    values['password'] = 'Alison'

    data = urllib.parse.urlencode(values)
    request = urllib.request.Request(url, data)
    response = urllib.request.urlopen(request)
    this_page = response.read().decode('utf-8')
    print(this_page)


# Data -get
def data_get():
    data = {}
    data['name'] = 'alison'
    data['passwd'] = '123'
    query_string = urllib.parse.urlencode(data)
    print(query_string)
    url = basic_url + '?' + query_string
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    print(html)
    print(response.geturl())


# Headers
# 用户代理（User-Agent）头
def header_demo():
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    values = {}
    values['name'] = 'alison'
    values['passwd'] = '123'
    data = urllib.parse.urlencode(values).encode('utf-8')
    headers = {'User-Agent': user_agent}
    req = urllib.request.Request(basic_url, data, headers)
    response = urllib.request.urlopen(req)
    page = response.read().decode('utf-8')
    print(page)
    print('------------info')
    print(response.info())
    print(req.data)


def handling_except():
    url = 'https://www.cnblogs.com/cxscode/p1/8179885.html'
    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req)
    except  URLError as e:
        print(e.reason)
        print(e.code)
        print(e.info())
        print(e.geturl())
        print(e.read().decode('utf-8'))


def handling_except_2():
    url = 'https://www.cnblogs.com/cxscode/p1/8179885.html'
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
    except IOError as e:
        if hasattr(e, 'reason'):
            print('failed to reach a server')
            print('reason', e.reason)
        if hasattr(e, 'code'):
            print('the server counln\'t fullfill the request')
            print(e.code)
        else:
            # do something
            code = response.getcode();
            print('code', code)


#  openers and handlers

handling_except_2()
