#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/25 22:40
# @Author  : alison
# @File    : task_master.py


import random, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()


def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
   pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
#  linux下运行成功， windows下出现问题
#  ForkingPickler(file, protocol).dump(obj)  序列化出现问题
# QueueManager.register('get_task_queue', callable=lambda: task_queue)
# QueueManager.register('get_result_queue', callable=lambda: result_queue)

# windows
QueueManager.register('get_task_queue', callable=return_task_queue)
QueueManager.register('get_result_queue', callable=return_result_queue)

# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey=b'asd')
# 启动Queue:
manager.start()

# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('try get results....')
for i in range(10):
    r = result.get(timeout=10)
    print('result: %s' % r)
# 关闭:
manager.shutdown()
print('master end')
