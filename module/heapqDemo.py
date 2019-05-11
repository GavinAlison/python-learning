#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 20:14
# @Author  : alison

'''
    heappush(heap, x)：将x压入对heap（这是一个列表）
    heappop(heap)：删除最小元素
    heapify()：将列表转换为堆
    heapreplace()  : 是heappop()和heappush()的联合，也就是删除一个，同时加入一个
'''
import heapq

print(heapq.__all__)

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 9)
heapq.heappush(heap, 2)
heapq.heappush(heap, 0)
heapq.heappush(heap, 11)
heapq.heappush(heap, 7)
heapq.heappush(heap, 5)
print(heap)

heapq.heappop(heap)

print(heap)

# heapq.heapify(heap) --->  将list转换成堆heap， return None
h1 = heapq.heapify(heap)
print(type(h1))
print(h1)
print(type(heap))
print(heap)

h1 = [2, 4, 6, 8, 9, 0, 1, 5, 3]
print(h1)
heapq.heapify(h1)
print(h1)

heapq.heapreplace(h1, 10)
print(h1)
