#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/23 9:20
# @Author  : alison
# @File    : 16.py

#  python多继承（新式类）一
class A(object):
    def foo(self):
        print('A foo')


class B(object):
    def foo(self):
        print('B foo')

    def bar(self):
        print('B bar')


class C1(A, B):
    pass


class C2(A, B):
    def bar(self):
        print('C2-bar')


class D(C1, C2):
    pass


if __name__ == '__main__':
    print(D.__mro__)  # 只有新式类有__mro__属性，告诉查找顺序是怎样的
    d = D()
    d.foo()
    d.bar()
# 其实新式类的搜索方法是采用了“广度优先”的方式去查找属性。
#
# 只有新式类有__mro__属性，该属性标记了python继承层次中父类查找的顺序，python多重继承机制中就是按照__mro__的顺序进行查找，一旦找到对应属性，则查找马上返回。

# 经过上面的__mro__输出可以发现，D类的继承查找路径为：D=>C1=>C2=>A=>B=>object，通过该查找路径，foo方法将会调用A的foo方法，、bar方法将调用C2的方法，通过实际实验调用，查看输出内容确实与__mro__顺序一样。
