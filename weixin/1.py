#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 19:56
# @Author  : alison
# @File    : 1.py


# coding:utf-8
import itchat

@itchat.msg_register
def text_reply(msg):
    print(msg)
    itchat.send(msg['Text'], msg['FromUserName'])


# 二维码
itchat.auto_login(hotReload=True)
itchat.run()
