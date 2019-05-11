#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 21:42
# @Author  : alison
# @File    : paramDemo.py4


#  传递参数练习


def foo(**args):
    print(args)


if __name__ == "__main__":
    foo(a=1, b=2, c=3)


#      #注意观察这次赋值的方式和打印的结果


# 另外一种传值方式

def add(x, y):
    return x + y

# 这有点像前面收集参数的逆过程
# 注意的是，元组中元素的个数，要跟函数所要求的变量个数一致。如果这样：
bars = (2, 3)
res = add(*bars)
print(res)



