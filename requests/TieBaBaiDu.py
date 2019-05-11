#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 21:48
# @Author  : alison
# @File    : BDTB.py


# 百度贴吧的爬取类

'''
需求：
    一句话需求： 爬取百度贴吧并进行存储
    详细需求：
1. 爬取贴吧：中国好声音吧，贴吧的名称、目录、关注数、帖子数、
吧主， 小吧主， 昵称，人数，
2. 查看贴吧中帖子
    帖子标题、楼数、发起者、结束者、帖子一楼内容, 记录楼主之后的五条(之内)记录
    标注几楼，回复者，时间，回复者等级
    帖子数，能实现翻页，
3.存储
    存储到文件中，起名: 贴吧名+时间戳.txt文件， 格式 写入时间+程序文件名+内容
    大小超过2M文件，分文件存储

'''

import urllib.request, re


class StringUtil:
    replaceTD = re.compile('<td>')
    replaceBR = re.compile('<br/>|<br>|<br/><br/>')
    replaceBlank = re.compile('\s+')

    def replace(self, x):
        x = re.sub(self.replaceTD, '\t', x)
        x = re.sub(self.replaceBR, '\n', x)
        x = re.sub(self.replaceBlank, '', x)
        return x.strip()


class TieBaBaiDu:
    def __init__(self):
        self.value = {}
        self.value['kw'] = '中国好声音'
        self.value['red_tag'] = 'g3268421752'
        self.value['fr'] = 'search'
        self.value['ie'] = 'utf-8'
        self.value['fn'] = 0
        self.value['timeout'] = 30
        self.tiebaBaiduUri = 'http://tieba.baidu.com/f'
        self.tiebaBaiduUrl = (self.tiebaBaiduUri + '?' + urllib.parse.urlencode(self.value)).encode('utf-8')
        self.pageIndex = 1
        self.headers = {}
        self.headers[
            'User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        self.headers['Connection'] = 'keep-alive'

        # 获取贴吧信息

    def getTieBaContent(self, uri, queryData, pageIndex):
        queryData['fn'] = pageIndex
        url = (uri + '?' + urllib.parse.urlencode(queryData))
        request = urllib.request.Request(url, headers=self.headers)
        response = urllib.request.urlopen(url)
        page = response.read().decode('utf-8')
        return page

    # 1. 爬取贴吧：中国好声音吧，贴吧的名称、目录、关注数、帖子数、
    # 吧主， 小吧主， 昵称，人数，
    def getBazhu(self, page):
        regex_tieba_name = r'<div class="card_top clearfix.*?class=" card_title_fname".*?>(.*?)</a>.*?class="card_num".*?<span class="card_menNum".*?>(.*?)</span>.*?class="card_infoNum">(.*?)</span>.*?<div class="card_info">.*?<a.*?>(.*?)</a>'
        pattern = re.compile(regex_tieba_name, re.S)
        items = re.findall(pattern, page)
        tool = StringUtil()
        itemList = []
        for item in items:
            for it in item:
                it = tool.replace(it)
                itemList.append(it)
        return itemList

    def start(self):
        BazhuItem = []
        uri = self.tiebaBaiduUri
        queryData = self.value
        pageIndex = self.pageIndex
        page = self.getTieBaContent(uri, queryData, pageIndex)
        BazhuItem = self.getBazhu(page)
        # 存储为[{key: value, key1: value1}]json形式
        print(BazhuItem)


t = TieBaBaiDu()
t.start()
