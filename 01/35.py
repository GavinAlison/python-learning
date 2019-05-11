#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 9:20
# @Author  : alison
# @File    : 16.py

# 多线程
# 多任务可以由多进程完成，也可以由一个进程内的多线程完成。
# 我们前面提到了进程是由若干线程组成的，一个进程至少有一个线程。

import time, threading


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended' % threading.current_thread().name)


print('thread %s is running....' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended ' % threading.current_thread().name)



