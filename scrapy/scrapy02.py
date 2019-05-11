#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/11 8:35
# @Author  : alison
# @File    : scrapy02.py


import re
import requests
import csv


def testMatch():
    str = 'www.runoob.com'
    regex = 'www'
    print(re.match(regex, str).span())
    print(re.match('com', str))


# 结果
# ![re1](resource/re-01.png)


def test01():
    line = 'cats are smarter than dogs'
    # .*代表匹配除换行符之外的所有字符
    # (.*?)第二个匹配分组, 非贪恋的
    # re.I 忽略大小写
    # re.M 多行模式
    matchObj = re.match(r'(.*)are(.*?).*', line, re.M | re.I)
    if matchObj:
        print('matchObj.group(): ', matchObj.group())
        print('matchObj.group(1): ', matchObj.group(1))
        print('matchObj.group(2): ', matchObj.group(2))
    else:
        print('Nothing found!')


def search():
    print(re.search('www', 'www.runoob.com').span())
    print(re.search('com', 'www.runoob.com').span())


def sub():
    phone = '500-234-222 # 号码'
    num = re.sub(r'#.*$', '', phone)
    print('号码:', num)
    #  \D 匹配非数字
    num = re.sub(r'\D', '', num)
    print('号码:', num)


def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)


def sub2():
    s = 'A12F45S98'
    # ?P<value> 代表为group分组，添加一个分组名
    print(re.sub('(?P<value>\d+)', double, s))
    # 记住要加?号
    print(re.sub('(P<value>\d+)', double, s))


# 结合requests、re两者的内容爬取 https://movie.douban.com/top250 中的内容，要求抓取名次、影片名称、国家、导演等字段。
def get_html(url):
    headers = {}
    headers[
        'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    if res.status_code == 200:
        return res.text
    return None

def get_info(html):
    pattern = re.compile(r'<li.*?<em class="">(.*?)</em>.*?<span class="title">(.*?)</span>.*?导演:(.*?)&nbsp;&nbsp;(.*?)<br>(.*?)&nbsp;/&nbsp;(.*?)&nbsp;/&nbsp;(.*?).*?</p>.*?<div class="star">.*?<span class="rating_num" property="v:average">(.*?)</span>.*?<span>(.*?)人.*?</li>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        index = re.sub(re.compile('\s+'), '', item[0])
        movie_name = re.sub(re.compile('\s+'), '', item[1])
        country = re.sub(re.compile('\s+'), '', item[5])
        # director = re.sub(re.compile('\s+'), '', item[2])
        director = item[2].strip()
        score = re.sub(re.compile('\s+'), '', item[7])
        # 一个带有 yield 的函数就是一个 generator
        writer.writerow([item[0], item[1], item[5], item[2], item[7]])
        print({
            'index': index,
            'movie_name': movie_name,
            'country': country,
            'director': director,
            'score': score
        })


if __name__ == '__main__':
    file = open('G:/NLP/movie.csv', 'w+', encoding='utf-8', newline='')
    writer = csv.writer(file)
    writer.writerow(['index', 'movie_name', 'country', 'director', 'score'])
    for i in range(10):
        url = 'https://movie.douban.com/top250?start=%d&filter=' % (i * 25)
        html = get_html(url)
        get_info(html)
