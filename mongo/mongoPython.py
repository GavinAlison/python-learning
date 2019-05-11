#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 20:42
# @Author  : alison
# @File    : mongoPython.py


# python利用mongodb上传图片数据 : GridFS 与 bson两种方式
#
# GridFS将图片数据与图片属性数据分开保存，用chunks来保存图片数据，files保存属性数据，一个图片file可能对应多个chunks，每个chunk的内存大小固定（16M），若图片数据大于chunk，则分为多个chunk保存，用同一个ObjectID关联，下载时自动将多个chunk合并为图片数据。


from pymongo import MongoClient
import gridfs


def mongoTest01():
    # 连接mongodb
    client = MongoClient('localhost', 27017)
    # 连接对应数据库
    db = client.infos
    # 连接collection
    fs = gridfs.GridFS(db, collection='images')
    num = 1
    for grid_out in fs.find(no_cursor_timeout=True):
        # 获取图片数据
        data = grid_out.read()
        outf = open('e:/temp/image/$d.jpg' % num, 'wb+')
        outf.write(data)
        outf.close()
        if num % 10000 == 0:
            metadata_file = open('e:/temp/metadata/%d.csv' % (num / 10000 + 1), 'ab+')
            csv_writer = csv.write(metadata_file, delimiter='\t')
        row = [grid_out.photo_title.encode('utf-8'), grid_out.uploadDate, \
               grid_out.upload_date, grid_out.longitude, grid_out.latitude, \
               grid_out.width, grid_out.height, grid_out.owner_name.encode('utf-8'), \
               grid_out.photo_id, grid_out._id, grid_out.photo_url]
        csv_writer.writerow(row)


# ---------------------------
# -----------000000----------
# ---------------------------
client = MongoClient('localhost', 27017)
db = client.infos
fs = gridfs.GridFS(db)

listfs = fs.list()
print(listfs)
file_id = 11
fs.get(file_id)


# ---------------------------
# -----------2222222----------
# ---------------------------
from bson import binary
from pymongo import MongoClient
import requests


def mongoTest02():
    client = MongoClient('localhost', 27017)
    db = client.infos
    image_collection = db.images
    dic = {}
    data = requests.get(dic['photo_url'], timeout=10).content
    if not image_collection.find_one({'photo_url': dic['photo_url']}):
        dic['imagecontent'] = binary.Binary(data)
        image_collection.insert(dic)
