#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 19:20
# @Author  : alison

# 简单的微信自动回复功能
import itchat
import requests
import re


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


@itchat.msg_register(['Text', 'Map', 'Card', 'Note', 'Sharing', 'Picture'])
def text_reply(msg):
    if not msg['FromUserName'] == Name['Mr.']:
        url = 'http://www.tuling123.com/openapi/api?key=2e1a074fb4b148ebb9556f0a70c1c588&info='
        url = url + msg['Text']
        html = getHtmlText(url)
        message = re.findall(r'\"text\":\".*?\"', html)
        print('----message----')
        print(message)
        reply = eval(message[0].split(':')[1])
        return reply


if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=True)
    friends = itchat.get_friends(update=True)[0:]
    Name = {}
    Nic = []
    User = []
    for i in range(len(friends)):
        Nic.append(friends[i]['NickName'])
        User.append(friends[i]['UserName'])
    print('----User -------')
    print(User)
    print('----Nic------')
    print(Nic)
    for i in range(len(friends)):
        Name[Nic[i]] = User[i]
    print('----Name------')
    print(Name.items())
    itchat.run()
