#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/19 11:51
# @Author  : alison
# @File    : StringUtils.py


# 处理字符的工具包

import re


class StringUtils:
    replaceTD = re.compile('<td>')
    replaceBR = re.compile('<br/>|<br>|<br/><br/>')

    def replace(self, x):
        x = re.sub(self.replaceTD, '\t', x)
        x = re.sub(self.replaceBR, '\n', x)
        x = x.strip()
