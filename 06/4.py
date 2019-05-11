#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/2 21:59
# @Author  : alison
# @File    : 4.py

import asyncio.coroutine


@asyncio.coroutine
def hello():
    print("Hello world!")
    r = yield from asyncio.sleep(1)
    print("Hello again!")


async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")
