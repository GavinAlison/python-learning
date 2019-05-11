#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 20:22
# @Author  : alison
# @File    : 4.py
# !/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import calendar

"""
    时间元组（年、月、日、时、分、秒、一周的第几日、一年的第几日、夏令时）
        一周的第几日: 0-6
        一年的第几日: 1-366
        夏令时: -1, 0, 1
"""

"""
    python中时间日期格式化符号：
    ------------------------------------
    %y 两位数的年份表示（00-99）
    %Y 四位数的年份表示（000-9999）
    %m 月份（01-12）
    %d 月内中的一天（0-31）
    %H 24小时制小时数（0-23）
    %I 12小时制小时数（01-12）
    %M 分钟数（00=59）
    %S 秒（00-59）
    %a 本地简化星期名称
    %A 本地完整星期名称
    %b 本地简化的月份名称
    %B 本地完整的月份名称
    %c 本地相应的日期表示和时间表示
    %j 年内的一天（001-366）
    %p 本地A.M.或P.M.的等价符
    %U 一年中的星期数（00-53）星期天为星期的开始
    %w 星期（0-6），星期天为星期的开始
    %W 一年中的星期数（00-53）星期一为星期的开始
    %x 本地相应的日期表示
    %X 本地相应的时间表示
    %Z 当前时区的名称  # 乱码
    %% %号本身
"""

#time.clock()
# （1）当前时间戳
# 1538271871.226226
print('=====1=======')
print(time.time())

# （2）时间戳 → 时间元组，默认为当前时间
# time.struct_time(tm_year=2018, tm_mon=9, tm_mday=3, tm_hour=9, tm_min=4, tm_sec=1, tm_wday=6, tm_yday=246, tm_isdst=0)
print('=====2=======')
print(time.localtime())
print(time.localtime(1538271871.226226))
print(time.localtime(time.time()))

# （3）时间戳 → 可视化时间
# time.ctime(时间戳)，默认为当前时间
print('=====3=======')
print(time.ctime(1538271871.226226))
print(time.ctime(time.time()))

# （4）时间元组 → 时间戳
# 1538271871
print('=====4=======')
print(time.mktime((2018, 9, 30, 9, 44, 31, 6, 273, 0)))

# （5）时间元组 → 可视化时间
# time.asctime(时间元组)，默认为当前时间
print('=====5=======')
print(time.asctime())
print(time.asctime((2018, 9, 30, 9, 44, 31, 6, 273, 0)))
print(time.asctime(time.localtime(1538271871.226226)))

# （6）时间元组 → 可视化时间（定制）
# time.strftime(要转换成的格式，时间元组)
print('=====6=======')
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# （7）可视化时间（定制） → 时间元祖
# time.strptime(时间字符串，时间格式)
print('=====7=======')
print(print(time.strptime('2018-9-30 11:32:23', '%Y-%m-%d %H:%M:%S')))

# （8）浮点数秒数，用于衡量不同程序的耗时，前后两次调用的时间差
#time.clock()

