#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 20:26
# @Author  : alison
# @File    : ExceptError.py


# 当程序出现错误，python会自动引发异常，也可以通过raise显示地引发异常。一旦执行了raise语句，raise后面的语句将不能执行。
class ExceptError():
    def test01(self):
        try:
            s = None
            if s is None:
                print('s is null')
                raise NameError  # 如果引发NameError异常，后面的代码将不能执行
            print(len(s))  # 这句不会执行，但是后面的except还是会走到
        except TypeError as e:
            print(e)
            pass

    def me(self, level):
        if level < 1:
            raise Exception('Invalid Level')
        # 触发异常后，后面的代码就不会再执行

    def test02(self):
        try:
            self.me(0)
        except Exception as  err:
            print(err)
        else:
            print(2)


a = ExceptError()
a.test02()
