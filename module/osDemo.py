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
# filePath = 'G:\\workspace\\PycharmProjects\\module\\resource'
filePath = 'D:\\workspace\\python-learning\\module\\resource'

for i in os.listdir(filePath):
    print(i)

cwd = os.getcwd()
print(cwd)
os.chdir(os.pardir)
cwd = os.getcwd()
print(cwd)

# os.makedirs('G:\\workspace\\PycharmProjects\\module\\resource\\1\\2')
os.chdir('.\\module\\resource\\1')

print(os.getcwd())
print('----------------')
# os.removedirs('G:\\workspace\\PycharmProjects\\module\\resource\\1')
# current  directory
path = 'G:\\workspace\\PycharmProjects\\module\\resource\\2.txt'
path = 'D:\\workspace\\python-learning\\module\\resource\\2.txt'
stat = os.stat(path)
print(stat)
print(type(stat))

mt = stat[8]
mt_time = time.ctime(mt)
print(mt_time)

print('----------os.system-------------')
os.system('chcp 65001')
command_str = os.system('dir')
print(type(command_str))
print('command_str==' + str(command_str))

print('-----start explorer-----')
# command_str = '"D:\\tool\\Mozilla Firefox\\firefox.exe"'
# os.system(command_str)


# ------  web助手
# webbrowser.open('https://www.baidu.com')

print('-------start os.path------')
join_path = os.path.join('d:/', 'workspace')
print(join_path)
'''
os.path.isabs(path)
os.path.isfile(path)
os.path.isdir(path)
os.path.islink(path)
os.path.ismount(path)
os.path.join(path1, path2 [, ...])
os.path.normpath(path)
'''
