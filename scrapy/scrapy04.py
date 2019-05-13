#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 23:05
# @Author  : alison
# @File    : scrapy04.py

# 使用lxml+xpath提取内容
# >https://blog.csdn.net/naonao77/article/details/88129994

import requests
from lxml import etree


def run():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    }
    url = 'http://www.dxy.cn/bbs/thread/626626#626626'
    res = requests.get(url, headers=headers)
    tree = etree.HTML(res.text)
    names = tree.xpath('//div[@class="auth"]/a/text()')
    create_times = tree.xpath('//div[@class="post-info"]/span/text()')
    del create_times[1]
    del create_times[1]
    contents = tree.xpath('//td[@class="postbody"]/text()')
    for content in contents:
        print(content.strip())
    result = []
    for i in range(len(names)):
        dictTmp = {'name': names[i].strip(), 'create_time': create_times[i].strip(), 'content': contents[i].strip()}
        print(dictTmp)
        print('*' * 80)
    result.append(dictTmp)


if __name__ == '__main__':
    run()
