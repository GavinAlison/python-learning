#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-01-03 22:46:00
# @Author  : alison
# @File    : fetch_qsbk2.py

#  备注： urllib2在python3.x版本里面，与urllib合并，以后导入urllib2，=import urllib.request
#  环境： python3.7.0
#  工具： pycharm2018.3

import urllib
import urllib.request
import re


##  设计面向对象模式

# page = 1
# url = 'https://www.qiushibaike.com/text/page/' + str(page) + '/'
# user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/71.0.3578.98 Safari/537.36'
# headers = {'User-Agent': user_agent}
#   抓取一下糗事百科的热门段子吧
#  抓取的内容为， 用户名， 用户内容，好笑数， 评论数
# regex2 = r'<a href="/users/\d+/".*?<h2>(.*?)</h2>.*?<a href="/article/\d+".*?<span>(.*?)</span>.*?<span class="stats-vote">.*?<i class="number">(.*?)</i>.*?<a href="/article/\d+.*?<i class="number">(.*?)</i>'


# try:
#     request = urllib.request.Request(url, headers=headers)
#     response = urllib.request.urlopen(request)
#     content = response.read().decode('utf-8')
#     # print(content)
#     pattern = re.compile(regex2, re.S)
#     items = re.findall(pattern, content)
#     print(items) # '''items的值为[(,,),(,,),(,,)], []匹配到list, ()为匹配到的元祖，()里面的值为匹配到的(.*?)匹配到的值'''
#     for item in items:
#         print('用户名: ', str(item[0]).replace('\n', ''))
#         print('内容: ', str(item[1]).replace('\n', '').replace('<br/>', '\n'))
#         print('好笑: ', str(item[2]))
#         print('评论: ', str(item[3]))
#         print()
# except Exception as e:
#     print(e)
# 糗事百科的爬虫
class QSBK:
    # 初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        # 初始化headers
        self.headers = {'User-Agent': self.user_agent}
        # 抓取一下糗事百科的热门段子
        #  抓取的内容为， 用户名， 用户内容，好笑数， 评论数
        self.regex = r'<a href="/users/\d+/".*?<h2>(.*?)</h2>.*?<a href="/article/\d+".*?<span>(.*?)</span>.*?<span class="stats-vote">.*?<i class="number">(.*?)</i>.*?<a href="/article/\d+.*?<i class="number">(.*?)</i>'
        # 存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        # 存放程序是否继续运行的变量
        self.enable = False

    # 传入某一页的索引获得页面代码
    def getPage(self, pageIndex):
        try:
            url = 'https://www.qiushibaike.com/text/page/' + str(pageIndex) + '/'
            request = urllib.request.Request(url, headers=self.headers)
            response = urllib.request.urlopen(request)
            pageContext = response.read().decode('utf-8')
            return pageContext
        except urllib.request.URLError as e:
            print('connect fail  ', e.reason)
            return None

    # 传入某一页代码
    def getPageItems(self, pageIndex):
        pageContext = self.getPage(pageIndex)
        if not pageContext:
            print('页面加载失败......')
            return None
        regex = self.regex
        pattern = re.compile(regex, re.S)
        items = re.findall(pattern, pageContext)
        # 用来存储每页的段子
        pageStories = []
        for item in items:
            # item存储的是用户名， 用户内容，好笑数， 评论数
            text1 = re.sub(r'\n', '', item[0])
            text2 = re.sub(r'\n', '', item[1])
            text3 = re.sub(r'\n', '', item[2])
            text4 = re.sub(r'\n', '', item[3])
            text2 = re.sub(r'<br/>', '\n', text2)
            t_tuple = (text1, text2, text3, text4)
            pageStories.append(t_tuple)
        return pageStories

    # 加载并提取页面的内容，加入到列表中
    def loadPage(self):
        # 如果当前未看的页数少于2页，则加载新一页
        if self.enable == True:
            if len(self.stories) < 2:
                # 获取新一页
                pageStories = self.getPageItems(self.pageIndex)
                # 将该页的段子存放到全局list中
                if pageStories:
                    self.stories.append(pageStories)
                    # 获取完之后页码索引加一，表示下次读取下一页
                    self.pageIndex += 1

    # 调用该方法，每次敲回车打印输出一个段子
    def getOneStory(self, pageStories, page):
        # 遍历一页的段子
        # print(pageStories)
        for story in pageStories:
            # print('story===',story)
            # 等待用户输入
            i = input()
            # 每当输入回车一次，判断一下是否要加载新页面
            self.loadPage()
            # 如果输入1则程序结束
            if i == "q":
                self.enable = False
                return
            print("第%d页\n\t发布人:\n\t\t%s\n\t内容:\n\t\t%s\n\t好笑数:\n\t\t%s\n\t评论数:\n\t\t%s\n" % (
                page, story[0], story[1], story[2], story[3]))

    #  print("第%d页\t发布人:%s\t内容:%s\t好笑数:%s\t评论数:%s\n" % (page, story[0], story[1], story[2], story[3]))
    # IndexError: string index out of range
    def start(self):
        print(u"正在读取糗事百科,按回车查看新段子，Q退出")
        # 使变量为True，程序可以正常运行
        self.enable = True
        # 先加载一页内容
        self.loadPage()
        # 局部变量，控制当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                # 从全局list中获取一页的段子
                pageStories = self.stories[0]
                # 当前读到的页数加一
                nowPage += 1
                # 将全局list中第一个元素删除，因为已经取出
                del self.stories[0]
                # 输出该页的段子
                self.getOneStory(pageStories, nowPage)


spider = QSBK()
spider.start()
