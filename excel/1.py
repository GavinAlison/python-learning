#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/3 20:33
# @Author  : alison
# @File    : 1.py

# openpyl
'''
Python   xls 的处理工具openpyxl
具体的工具详见:
https://www.cnblogs.com/paul-liang/p/9187503.html
工具有： XlsxWriter、xlrd、xlwt、xlutils、openpyxl、microsoft excel api


openpyxl模块是解决Microsoft Excel 2007/2010之类版本的excel
扩展名是Excel 2010 xlsx/xlsm/xltx/xltm的文件的读写的第三方库。
'''

import xlsxwriter

# create an new excel file and add a worksheet
workbook = xlsxwriter.Workbook(filename='.//resource//demo.xlsx')
worksheet = workbook.add_worksheet()
# widen the first column to make the text clearer
worksheet.set_column('A:A', 20)
# add a bold format to use to highlight cells
bold = workbook.add_format({'bold': True})
worksheet.write('A1', 'hello')
# text with formatting
worksheet.write('A2', 'world', bold)
# writer some numbers , woth row/column notation
worksheet.write(2, 0, 123)  # C3:A1
worksheet.write(3, 0, 123.456)  # D4:A1
#  insert an image
# worksheet.insert_image('B5', 'log.png')
workbook.close()
