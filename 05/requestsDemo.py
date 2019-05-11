#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 21:27
# @Author  : alison
# @File    : requestsDemo.py


import requests

# GET
r = requests.get('https://www.douban.com/')
print(r.status_code)
print(r.text)
#  get params
param = {'q': 'python', 'cat': '100'}
url = 'https://www.douban.com'
r = requests.get(url, params=param)
print(r.url)
print(r.content)
#  get json
r = requests.get(
    'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())

print('---------------------------')
#  post
r = requests.post('https://accounts.douban.com/login',
                  data={'form_email': 'abc@example.com', 'form_password': '123456'})

params = {'key': 'value'}
r = requests.post(url, json=params)
print(r.url)
print(r.request)

upload_files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=upload_files)
print(r.text)







