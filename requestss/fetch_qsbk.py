#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/20 21:00
# @Author  : alison
# @File    : fetch_qsbk.py

#  备注： urllib2在python3.x版本里面，与urllib合并，以后导入urllib2，=import urllib.request
#  环境： python3.7.0
#  工具： pycharm2018.3

import urllib
import urllib.request
import re

##  编写一个正则，出错，还是去查看一下为啥出错
##  初步判定是regex正则出错
#   2019-01-03  判断出问题
#   原来items = re.findall(pattern, str)方法不熟悉，可以多了解一下，
#   findall(pattern , str)匹配的为pattern中的字符，取出items, items[0][0]为匹配到pattern中分组信息

page = 1
url = 'https://www.qiushibaike.com/text/page/' + str(page) + '/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/71.0.3578.98 Safari/537.36'
headers = {'User-Agent': user_agent}
regex = r'<div.*?class="article block untagged mb15.*?>.*?<a.*?/a><a.*?>.*?<h2>(.*?)</h2>.*?</a>.*?<span>(.*?)</span>.*?</div>.*'
regex1 = r'<div id="(.*?)" class="main">'
#   抓取一下糗事百科的热门段子吧
#  抓取的内容为， 用户名， 用户内容，好笑数， 评论数
regex2 = r'<a href="/users/\d+/".*?<h2>(.*?)</h2>.*?<a href="/article/\d+".*?<span>(.*?)</span>.*?<span class="stats-vote">.*?<i class="number">(.*?)</i>.*?<a href="/article/\d+.*?<i class="number">(.*?)</i>'
# 现在正则表达式在这里稍作说明
#
# 1）.*? 是一个固定的搭配，.和*代表可以匹配任意无限多个字符，加上？表示使用非贪婪模式进行匹配，也就是我们会尽可能短地做匹配，以后我们还会大量用到 .*? 的搭配。
#
# 2）(.*?)代表一个分组，在这个正则表达式中我们匹配了五个分组，在后面的遍历item中，item[0]就代表第一个(.*?)所指代的内容，item[1]就代表第二个(.*?)所指代的内容，以此类推。
#
# 3）re.S 标志代表在匹配时为点任意匹配模式，点 . 也可以代表换行符。
try:
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    # print(content)
    pattern = re.compile(regex2, re.S)
    items = re.findall(pattern, content)
    print(items) # '''items的值为[(,,),(,,),(,,)], []匹配到list, ()为匹配到的元祖，()里面的值为匹配到的(.*?)匹配到的值'''
    for item in items:
        print('用户名: ', str(item[0]).replace('\n', ''))
        print('内容: ', str(item[1]).replace('\n', '').replace('<br/>', '\n'))
        print('好笑: ', str(item[2]))
        print('评论: ', str(item[3]))
        print()
except Exception as e:
    print(e)
    # 糗事百科的爬虫
    # class QSBK:
    #     def __init__(self):
    #         self.pageIndex = 1
    #         self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    #         self.headers = {'User-Agent': self.user_agent}
    #         self.stories = []
    #         self.enable = False
    #
    #     def getPageUrl(self,pageIndex):
    #         try:
    #             url = 'https://www.qiushibaike.com/text/page/' + str(pageIndex) + '/'
    #             request = urllib.request.Request(url,headers=self.headers)
    #             response = urllib.request.urlopen(request)
    #             pageCode = response.read().decode('utf-8')
    #             return pageCode
    #         except urllib.request.URLError:
    #             print('connect fail')
    #             return None
    #
    #     def getPageItems(self,pageIndex):
    #         pageContext = self.getPage(pageIndex)
    #         if not page:
    #             print('页面加载失败......')
    #             return None
    #         regex = r'<div.*?article.*?block.*?untagged.*?mb15.*?>.*?<h2>(.*?)</h2>.*?<span>(.*?)</span></div>'
    #         pattern = re.compile(regex,re.S)
    #         items = re.findall(pattern,pageContext)
    #         pageStories = []
    #         for item in items:
    #             pageStories.append(item[0].strip(),'\n')
    #         return pageStories
    #
    #     def start(self):
    #         for i in range(1,11):
    #             self.stories.append(self.getPageItems(i))
    #         for y in self.stories:
    #             print(y)
    # spider = QSBK()
    # spider.start()
