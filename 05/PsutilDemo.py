#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/26 21:52
# @Author  : alison
# @File    : PsutilDemo.py


import psutil

# CPU逻辑数量
# r = psutil.cpu_count()
# print(r)
# CPU物理核心
# r = psutil.cpu_count(logical=False)
# print(r)
# 统计CPU的用户／系统／空闲时间：
# r = psutil.cpu_times()
# print(r)
# 实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
# for x in range(10):
#     r = psutil.cpu_percent(interval=1, percpu=True)
#     print(r)

# 使用psutil获取物理内存和交换内存信息
# r = psutil.virtual_memory()
# print(r)
# r = psutil.swap_memory()
# print(r)

# psutil获取磁盘分区、磁盘使用率和磁盘IO信息：
# 磁盘分区信息
# r = psutil.disk_partitions()
# print(r)
# # 磁盘使用情况
# r = psutil.disk_usage('C:\\')
# print(r)
# # 磁盘IO
# r = psutil.disk_io_counters()
# print(r)
# 获取网络读写字节／包的个数
# r = psutil.net_io_counters()
# print(r)
# 获取网络接口信息
# r = psutil.net_if_addrs()
# print(r)
# 获取网络接口状态
# r = psutil.net_if_stats()
# print(r)

# r = psutil.net_connections()
# print(r)


# 获取进程信息
# 所有进程ID
# r = psutil.pids()
# print(r)
# # 获取指定进程ID=1396，其实就是当前Python交互环境
# p = psutil.Process(16820)
# print(p)
# # 进程名称
# print(p.name())
# # 进程exe路径
# print(p.exe())
# # 进程工作目录
# print(p.cwd())
# # 进程启动的命令行
# print(p.cmdline())
# # 父进程ID
# print(p.ppid)
# # 父进程
# p.parent()
# # 子进程列表
# p.children()
# # 进程状态
# print(p.status())
# # 进程用户名
# print(p.username())
# # 进程创建时间
# print(p.create_time())
# # 进程终端
# # print(p.terminal())
# # 进程使用的CPU时间
# print(p.cpu_times())
# # 进程使用的内存
# print(p.memory_info())
# # 进程打开的文件
# print(p.open_files())
# # 进程相关网络连接
# print(p.connections())
# # 进程的线程数量
# print(p.num_threads())
# # 所有线程信息
# print(p.threads())
# 进程环境变量
# print(p.environ())
# NotImplementedError: NtWow64QueryVirtualMemory64 missing
# 结束进程
# p.terminate()


psutil.test()