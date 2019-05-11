#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/23 19:39
# @Author  : alison
# @File    : mysqlDemo.py

import pymysql as pm


def createTable():
    conn = pm.connect(host='localhost', user='root', password='root', database='employees', charset='utf8')
    cursor = conn.cursor()
    sql = """
    create table if not exists `employees`.`user1`(
        id int auto_increment primary key,
        name char(10) not null unique,
        age tinyint not null
    )engine=innodb default charset = utf8mb4;
    """
    res = cursor.execute(sql)
    print(res)
    cursor.close()
    conn.close()


# 返回字典格式数据：
def createTableForDict():
    conn = pm.connect(host='localhost', user='root', password='root', database='employees', charset='utf8')
    cursor = conn.cursor(cursor=pm.cursors.DictCursor)
    sql = """
       create table if not exists `user1`(
           id int auto_increment primary key,
           name char(10) not null unique,
           age tinyint not null
       )engine=innodb default charset = utf8mb4;
       """
    res = cursor.execute(sql)
    print(res)
    cursor.close()
    conn.close()


# 增删改查操作
def add():
    conn = pm.connect(host='localhost', user='root', password='root', database='employees', charset='utf8')
    cursor = conn.cursor()
    sql = """
          insert into user1(name, age) values(%s, %s)
           """
    username = 'alison'
    age = 22
    try:
        #   执行SQL语句
        res = cursor.execute(sql, [username, age])
        print(res)
        #  提交事务
        conn.commit()
    except Exception as e:
        # 有异常，回滚事务
        conn.rollback()
    cursor.close()
    conn.close()


def getId():
    conn = pm.connect(host='localhost', user='root', password='root', database='employees', charset='utf8')
    cursor = conn.cursor()
    sql = """
              insert into user1(name, age) values(%s, %s)
               """
    username = 'tom'
    age = 22
    try:
        #   执行SQL语句
        res = cursor.execute(sql, [username, age])
        print(res)
        #  提交事务
        conn.commit()
        last_id = cursor.lastrowid
        print(last_id)
    except Exception as e:
        # 有异常，回滚事务
        conn.rollback()
    cursor.close()
    conn.close()


def batchInsert():
    conn = pm.connect(host='localhost', user='root', password='root', database='employees', charset='utf8')
    cursor = conn.cursor()
    sql = """
                 insert into user1(name, age) values(%s, %s)
                  """
    data = [{'alison', 22}, {'gavin', 21}]
    try:
        #   执行SQL语句
        res = cursor.execute(sql, data)
        print(res)
        #  提交事务
        conn.commit()
    except Exception as e:
        # 有异常，回滚事务
        conn.rollback()
    cursor.close()
    conn.close()


def queryOne():
    conn = pm.connect(host='localhost', user='root', password='root', database='employees', charset='utf8')
    cursor = conn.cursor()
    sql = """
          select id , name,age from user1  where id = 1;
          """
    try:
        #   执行SQL语句
        res = cursor.execute(sql)
        print(res)
        ret = cursor.fetchone()
        print(ret)
        #  提交事务
        conn.commit()
    except Exception as e:
        # 有异常，回滚事务
        conn.rollback()
        print(e)
    cursor.close()
    conn.close()


def queryAll():
    conn = pm.connect(host='localhost', user='root', password='root', database='employees', charset='utf8')
    cursor = conn.cursor()
    sql = """
          select id , name, age from user1  ;
          """
    try:
        #   执行SQL语句
        res = cursor.execute(sql)
        print(res)
        ret = cursor.fetchall()
        print(ret)
        cursor.scroll(0, mode='absolute')
        print(cursor.fetchone())
        cursor.scroll(0, mode='absolute')
        res2T = cursor.fetchmany(3)
        print(res2T)
        #  提交事务
        conn.commit()
    except Exception as e:
        # 有异常，回滚事务
        conn.rollback()
    cursor.close()
    conn.close()


'''
# 光标按绝对位置移动1
cursor.scroll(1, mode="absolute")
# 光标按照相对位置(当前位置)移动1
cursor.scroll(1, mode="relative")
'''


def update():
    conn = pm.connect(host='localhost', user='root', password='root', database='employees', charset='utf8')
    cursor = conn.cursor()
    sql = """
          update  user1 set age=%s where name=%s ;
          """
    age = 33
    name = 'alison'
    try:
        #   执行SQL语句
        res = cursor.execute(sql, [age, name])
        print(res)
        #  提交事务
        conn.commit()
    except Exception as e:
        # 有异常，回滚事务
        conn.rollback()
        print(e)
    cursor.close()
    conn.close()


def delete():
    conn = pm.connect(host='localhost', user='root', password='root', database='employees', charset='utf8')
    cursor = conn.cursor()
    sql = """delete from `employees`.`user1` where name=%s ;
        """
    name = 'alison'
    try:
        #  执行SQL语句
        res = cursor.execute(sql, [name])
        print(res)
        #  提交事务
        conn.commit()
    except Exception as e:
        # 有异常，回滚事务
        conn.rollback()
        print(e)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    # createTable()
    # createTableForDict()
    # add()
    # getId()
    # batchInsert()
    # queryOne()
    # queryAll()
    # update()
    # queryAll()
    # delete()
    # queryAll()
    pass
