#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 20:22
# @Author  : alison
# @File    : statisticsWeiXin.py

#  统计微信好友信息
#  男女比例

import itchat, matplotlib.pyplot as plt


class friends_statistics(object):
    def __init__(self):
        self.sex_man = 0
        self.sex_woman = 0
        self.sex_other = 0
        self.sex_count = 0

    def fri_sex_statistics(self, friends):
        friendss = list(friends)
        self.sex_count = len(friends)
        for foo in friends[1:]:
            sex = foo["Sex"]
            if sex == 1:
                self.sex_man += 1
            elif sex == 2:
                self.sex_woman += 1
            else:
                self.sex_other += 1

    def draw_sex(self):
        man_ratio = int(self.sex_man) / self.sex_count * 100
        woman_ratio = int(self.sex_woman) / self.sex_count * 100
        other_ratio = int(self.sex_other) / self.sex_count * 100

        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        # =================================
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        # labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
        labels = '男', '女', '其他'
        # sizes = [15, 30, 45, 10]
        sizes = [man_ratio, woman_ratio, other_ratio]
        # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
        explode = (0, 0.1, 0)
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.show()
        # =================================
        # plt.figure(figsize=(5, 5))  # 绘制的图片为正圆
        # sex_li = ['男', '女', '其他']
        # radius = [0.01, 0.01, 0.01]  # 设定各项距离圆心n个半径
        # colors = ['red', 'yellowgreen', 'lightskyblue']
        # proportion = [man_ratio, woman_ratio, other_ratio]
        #
        # plt.pie(proportion, explode=radius, labels=sex_li, colors=colors, autopct='%.2f%')  # 绘制饼图
        # 加入图例 loc =  'upper right' 位于右上角 bbox_to_anchor=[0.5, 0.5] # 外边距 上边 右边 borderaxespad = 0.3图例的内边距
        # plt.legend(loc="upper right", fontsize=10, bbox_to_anchor=(1.1, 1.1), borderaxespad=0.3)
        # 绘制标题
        # plt.title('微信好友性别比例')
        # 展示
        # plt.show()


if __name__ == "__main__":
    itchat.auto_login(hotReload=True)
    friends = itchat.get_friends(update=True)[0:]
    # print(friends)
    # print(friends[0:1])
    # for foo in friends[0:1]:
    #     print(foo)
    f = friends_statistics()
    # friends = [{'Sex':1}]
    f.fri_sex_statistics(friends)
    f.draw_sex()
