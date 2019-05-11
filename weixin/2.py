#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/15 21:08
# @Author  : alison
# @File    : 2.py


import itchat
import requests
import json, random
from itchat.content import *


def tuling123(msg):
    url = "http://www.tuling123.com/openapi/api"
    info = msg
    key = "11d8a7c5e9564a3fa5217bdd9a868778"
    data = {u"key": key, 'info': info}
    r = requests.get(url, params=data)
    re = json.loads(r.text)
    return (re)


@itchat.msg_register(TEXT, isFriendChat=True, isMpChat=True)
def send_text(msg):
    te = tuling123(msg['Text'])
    itchat.send_msg(te['text'], msg['FromUserName'])


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    itchat.run()
