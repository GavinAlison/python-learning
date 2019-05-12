#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/12 18:11
# @Author  : alison
# @File    : BeautifulSoupDemo.py


from bs4 import BeautifulSoup as bs
import urllib.request


# 楼主， 发布时间， 发布内容
def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
    }
    url = 'http://www.dxy.cn/bbs/thread/626626#626626'
    request = urllib.request.Request(url, headers=headers)
    context = urllib.request.urlopen(request).read().decode('utf-8')
    #  指定解析器
    html = bs(context, 'lxml')
    # 用来存放获取的用户名、发布时间和评论
    datas = []
    try:
        names = html.select('div.auth')
        create_times = html.select('div.post-info span:first-child')
        contexts = html.select('td.postbody')
        for i in range(len(names)-1):
            name = names[i].get_text(strip=True)
            create_time = create_times[i].get_text(strip=True)
            context = contexts[i].get_text(strip=True)
            dictTmp = {'name': name, 'create_time': create_time, 'context': context}
            print(dictTmp)
            datas.append(dict)
    except BaseException as e:
        pass
    return datas
if __name__ == '__main__':
    main()