#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/28 21:55
# @Author  : alison
# @File    : gridfsDemo.py


'''
利用gridfs构建分布式大文件存储系统
'''
from pymongo import MongoClient
from gridfs import GridFS
import random
import os


class GFS(object):
    def __init__(self, ip, port, file_db, file_collection):
        self.ip = ip
        self.port = port
        self.file_db = file_db
        self.file_collection = file_collection

    def createDB(self):
        '''
        connection database, create db, create collection
        '''
        client = MongoClient(self.ip, self.port)
        db = client[self.file_db]
        file_collection = db[self.file_collection]
        return (db, file_collection)

    def insertFile(self, db, filePath, query):
        '''
        save file
        :param db:
        :param filePath:
        :param query:
        :return:
        '''
        fs = GridFS(db, self.file_collection)
        if fs.exists(query):
            print('alreay exists!')
        else:
            with open(filePath, 'rb') as fileObj:
                data = fileObj.read()
                ObjectId = fs.put(data, filename=filePath.split('/')[-1])
                print(ObjectId)
                fileObj.close()
            return ObjectId

    def queryId(self, db, query):
        '''
        通过文件属性获取文件id，id为文件删除，读取，下载做准备
        :param db:
        :param query:
        :return:
        '''
        fs = GridFS(db, self.file_collection)
        data = fs.find_one(query)
        return data._id

    def getFile(self, db, id):
        '''
        获取文件属性， 并读取二进制数据保存到新文件中
        :param db:
        :param id:
        :return:
        '''
        fs = GridFS(db, self.file_collection)
        gf = fs.get(id)
        bdata = gf.read()  # 二进制数据
        attri = {}  # 文件属性
        attri['chunk_size'] = gf.chunk_size
        attri['length'] = gf.length
        attri['upload_data'] = gf.upload_date
        attri['filename'] = gf.filename
        attri['md5'] = gf.md5
        print(attri)
        return (bdata, attri)

    def listFile(self, db):
        '''
        列出所有文件名
        :param db:
        :return:
        '''

        fs = GridFS(db, self.file_collection)
        gf = fs.list()
        return tuple(gf)

    def write2disk(self, bdata, attri):
        '''
        将二进制数据存入磁盘
        :param bdata:
        :param attri:
        :return:
        '''
        num = random.random()
        filePath = ('e:\\temp\\%d.log'%num)
        with open(filePath,  mode='ab') as fileObj:
            fileObj.write(bdata)
        print('fetch binary data!')

    def remove(self, db, id):
        '''
        删除文件数据
        :param db:
        :param id:
        :return:
        '''
        fs = GridFS(db, self.file_collection)
        fs.delete(id)


if __name__ == '__main__':
    gfs = GFS('localhost', 27017, 'fileDB', 'upload')
    (fileDb, fileTable) = gfs.createDB()
    filePath = 'e:\\temp\\1.png'
    query = {'filename': 'e:\\temp\\1.png'}
    gfs.insertFile(fileDb, filePath, query)
    id = gfs.queryId(fileDb, query)
    (bdata, attri) = gfs.getFile(fileDb, id)
    gfs.write2disk(bdata, attri)
    gfs.listFile(fileDb)
