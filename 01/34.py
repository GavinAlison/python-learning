#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 9:20
# @Author  : alison
# @File    : 16.py

# 进程间通信
from multiprocessing import Process, Queue
import os, time, random


# write process
def write(q):
    print('Process to write : %s' % os.getpid())
    for value in ['A', 'B', 'C', 'D']:
        print('put %s to queue....' % value)
        q.put(value)
        time.sleep(random.random())


# read process
def read(q):
    print('Process to read : %s' % os.getpid())
    while True:
        value = q.get(True)
        print('get %s from queue' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()
