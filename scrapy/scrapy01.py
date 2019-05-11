#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/11 8:35
# @Author  : alison
# @File    : scrapy01.py

# import requests

# help(requests.get)
# print("----------------------")
# help(requests.post)

# get请求
# url = 'https://www.baidu.com'
# response = requests.get(url)
# print(response.text)

# print('--------------分割线--------------')
# post 请求
# data = {
#     "name": "aa",
#     "school": 'linan'
# }
# response = requests.post(url, data=data)
# print(response.text)

import json

# data = {
#     "name": "aa",
#     "school": 'linan'
# }
#  将json对象转换成json字符串
# json_str = json.dumps(data)
# print(json_str)
# # 将json字符串转换成json对象
# data = json.loads(json_str)
# print(data)

# import urllib.request as ur

# print('--------ur.urlopen')
# # help(ur.urlopen)
#
#
# print('--------get')
# # get
# url = 'https://www.baidu.com'
# res = ur.urlopen(url)
# #  read first line
# fristline = res.readline()
# print(fristline)
#
# print('-------post')
# # post
# req = ur.Request(url=url, data=b'the first day of web crawler')
# res_data = ur.urlopen(req)
# res = res_data.read()
# print(res)


import urllib.request, urllib
from urllib.request import URLError
from io import BytesIO
import gzip

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
    print(html)


# Data  -post
def data_post():
    url = 'http://user.51sole.com/'
    values = {}
    values['txtUserName'] = '1'
    values['txtPwd'] = '1'

    data = urllib.parse.urlencode(values).encode('utf-8')
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
    print('-----query_string')
    print(query_string)
    url = basic_url + '?' + query_string
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    print(html)
    print('-----------response.url')
    print(response.geturl())


# Headers
# 用户代理（User-Agent）头
def header_demo():
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    values = {}
    values['name'] = 'alison'
    values['passwd'] = '123'
    data = urllib.parse.urlencode(values).encode('utf-8')
    headers = {'user-agent': user_agent}
    headers[
        'accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3'
    headers['accept-encoding'] = 'gzip, deflate, br'
    headers['accept-language'] = 'zh-CN,zh;q=0.9,en;q=0.8'
    headers['Connection'] = 'keep-alive'
    req = urllib.request.Request(basic_url, data, headers)
    response = urllib.request.urlopen(req)
    print('---------response.geturl')
    print(response.geturl())
    # 以“b'\x1f\x8b\x08”开头的数据是经过gzip压缩过的数据，这里当然需要进行解压了
    buff = BytesIO(response.read())
    f = gzip.GzipFile(fileobj=buff)
    page = f.read().decode('UTF-8')
    print('----------page')
    print(page)
    print('------------info')
    print(response.info())
    print('------------req.data')
    print(req.data)


def handling_except():
    url = 'https://www.cnblogs.com/cxscode/p/8228042.html'
    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req)
    except  URLError as e:
        print('------e.reason')
        print(e.reason)
        print('-----e.code')
        print(e.code)
        print('----------e.info()')
        print(e.info())
        print('----------e.geturl()')
        print(e.geturl())
        print("---------e.read().decode('utf-8')")
        print(e.read().decode('utf-8'))


def handling_except_2():
    url = 'https://www.cnblogs.com/cxscode/p/8228042.html'
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

# header_demo()
# get_url()
# get_url_2()
# url_info()
# data_post()
# data_get()
# handling_except()
handling_except_2()