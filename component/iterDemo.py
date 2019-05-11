#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/18 21:13
# @Author  : alison
'''
迭代器，讲通俗点就是可迭代对象只占一个内存地址，每次只抛出对象里的一个元素，优点是速度快，占内存少，而普通的做法是有多少个元素就占多少个地址。
'''


class Reverse:
    '''iterator for looping over a sequence  backwards '''

    def __init__(self, data):
        self.data = data
        self.index = len(data)
        # print(self.data[0])

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


if __name__ == '__main__':
    test = Reverse('hello')
    print(test.data)
    for char in test:
        print(char)
