#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 21:31
# @Author  : alison
# @File    : consumer.py
#   协程
#   协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。
#
#   注意，在一个子程序中中断，去执行其他子程序，不是函数调用，有点类似CPU的中断。比如子程序A、B：
#
#   协程本质
#   Python对协程的支持是通过generator实现的。
#   在generator中，我们不但可以通过for循环来迭代，还可以不断调用next()函数获取由yield语句返回的下一个值。

#   但是Python的yield不但可以返回一个值，它还可以接收调用者发出的参数。

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)