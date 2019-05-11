#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/21 21:38
# @Author  : alison
# @File    : osDemo.py


# 操作文件：重命名、删除文件
'''
    rename
    remove
    listdir
    os.getcwd, os.chdir：当前工作目录，改变当前工作目录
    os.makedirs, os.removedirs：创建和删除目录
'''
import os, time
import webbrowser


# os.rename('G:\\workspace\\PycharmProjects\\module\\resource\\1.txt', 
#            'G:\\workspace\\PycharmProjects\\module\\resource\\2.txt')

# os.remove('G:\\workspace\\PycharmProjects\\module\\resource\\a.txt')

for i in os.listdir('G:\\workspace\\PycharmProjects\\module\\resource'):
    print(i)

cwd = os.getcwd()
print(cwd)
os.chdir(os.pardir)
cwd = os.getcwd()
print(cwd)

# os.makedirs('G:\\workspace\\PycharmProjects\\module\\resource\\1\\2')
os.chdir('.\\module\\resource\\1')

print('----------------')
# os.removedirs('G:\\workspace\\PycharmProjects\\module\\resource\\1')
# current  directory
stat = os.stat('G:\\workspace\\PycharmProjects\\module\\resource\\2.txt')
print(stat)
print(type(stat))

mt = stat[8]
mt_time = time.ctime(mt)
print(mt_time)

print('----------os.system-------------')
command_str = os.system('dir')
print(type(command_str))
print('command_str==' + str(command_str))

print('-----start explorer-----')
command_str = '"D:\\tool\\Mozilla Firefox\\firefox.exe"'
# os.system(command_str)


# ------  web助手
webbrowser.open('https://www.baidu.com')

