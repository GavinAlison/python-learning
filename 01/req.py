#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/8 21:35
# @Author  : alison
# @File    : req.py

import urllib.request
import re
import os

#baidu_image = "https://image.baidu.com/"
#baidu_image1 = "https://image.baidu.com/search/detail?z=0&hs=0&pn=0&spn=0&di=0&pi=57912640036&tn=baiduimagedetail&is=0%2C0&ie=utf-8&oe=utf-8&cs=3859916625%2C1955794582&os=&simid=&adpicid=0&lpn=0&fm=&sme=&cg=&bdtype=-1&oriquery=&objurl=http%3A%2F%2Fe.hiphotos.baidu.com%2Fimage%2Fpic%2Fitem%2Fb151f8198618367afe76969623738bd4b21ce5fa.jpg&fromurl=&gsm=0&catename=pcindexhot&islist=&querylist=&word=%E8%8A%B1%E5%84%BF%E8%A7%86%E8%A7%89"
baidu_image2 = "https://image.baidu.com/search/detail?z=0&hs=0&pn=0&spn=0&di=0&pi=57912640036&tn=baiduimagedetail&is=0%2C0&ie=utf-8&oe=utf-8&cs=3859916625%2C1955794582&os=&simid=&adpicid=0&lpn=0&fm=&sme=&cg=&bdtype=-1&oriquery=&objurl=http%3A%2F%2Fe.hiphotos.baidu.com%2Fimage%2Fpic%2Fitem%2Fb151f8198618367afe76969623738bd4b21ce5fa.jpg&fromurl=&gsm=0&catename=pcindexhot&islist=&querylist=&word="
def crawler(keyword):
    quote_keyword = urllib.request.quote(keyword)
    url = baidu_image2 + keyword
    req =urllib.request.Request(url)
    req.add_header("User-Agent", '''Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36''')
    data = urllib.request.urlopen(req).read().decode()

    images = re.findall("\"objURL\":\"(.+?)\",",  data)
    return images[:60]

def download(keyword, images):
    count = len(images)
    os.mkdir(r"E:\{}").format(keyword)
    for i in range(count):
        try:
            f =r"e:\{0}\{0}{1}.jpg".format(keyword, i+1)
            urllib.request.urlretrieve(images[i], f)
        except  Exception as e:
            pass

###
images = crawler("迪丽热巴")
download("迪丽热巴", images)


## 失败......
