#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 22:36
# @Author  : alison
# @File    : list02.py


# list
#  1. insert(i, val)用法
#  2. pop(i), remove(val)用法
#  3. list.reverse()与list.sort(key, reverse=False)
'''
1. insert
与list.append(x)类似，list.insert(i,x)也是对list元素的增加。只不过是可以在任何位置增加一个元素。
如果遇到那个i已经超过了最大索引值，会自动将所要插入的元素放到列表的尾部，即追加。
2. pop(i)
    删除
   remove(val)
    删除the first item
-   如果正确删除，不会有任何反馈。没有消息就是好消息。并且是对列表进行原地修改。
-   如果所删除的内容不在list中，就报错。注意阅读报错信息：x not in list

'''
all_users = ['alison', 'gavin']
all_users.append('io')
print(all_users)
all_users.insert(0, 'ui')
print(all_users)
print(len(all_users))
all_users.insert(10, 'haha')
print(all_users)

print('--------------')
all_users = ['python', 'http://', 'qiwsir', 'github', 'io', 'algorithm']
print(all_users)
all_users.remove('http://')
print(all_users)
# all_users.remove("taobao")
# ValueError: list.remove(x): x not in list

lst = ['python', 'java', 'python', 'c', 'javscript']
print(lst)
lst.remove('python')
print(lst)
all_users = ['python', 'http://', 'qiwsir', 'github', 'io', 'algorithm']
item = all_users.pop()
print(item)
print(all_users)

# 简单总结一下，list.remove(x)中的参数是列表中元素，即删除某个元素；list.pop([i])中的i是列表中元素的索引值，这个i用方括号包裹起来，意味着还可以不写任何索引值，如上面操作结果，就是删除列表的最后一个。

a = [1, 2, 3, 4, 5, 6]
a.reverse()
print(a)
# 注意，是原地反过来，不是另外生成一个新的列表。所以，它没有返回值。跟这个类似的有一个内建函数reversed，建议读者了解一下这个函数的使用方法。
#
# 因为list.reverse()不返回值，所以不能实现对列表的反向迭代，如果要这么做，可以使用reversed函数。

a.sort()
print(a)
a.sort(reverse=True)
# 实现了从大到小的排序。
print(a)
# sort(...)
#
# L.sort(cmp=None, key=None, reverse=False) -- stable sort IN PLACE; cmp(x, y) -> -1, 0, 1
# key设置按照哪个关键字进行排序
lst = ["python", "java", "c", "pascal", "basic"]
lst.sort(key=len, reverse=True)
print(lst)
