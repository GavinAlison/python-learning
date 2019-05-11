#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/22 21:19
# @Author  : alison
# @File    : jsonDemo.py

import json


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Person Object name : %s , age : %s' % (self.name, str(self.age))


def object2dict(obj):
    '''
    convert Person to dict
    '''
    d = {}
    d['__class__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    return d


def dict2object(d):
    '''
    convert dict ot Person
    '''
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        print('module=='+str(module))
        class_ = getattr(module, class_name)
        print('class_name=='+str(class_name))
        print('class_=='+str(class_))
        # get args
        args = dict((key.encode('ascii'), value) for key, value in d.items())
        print(args)
        # create new instance
        inst = class_(*args)
        print(inst)
    else:
        inst = d
    return inst


if __name__ == '__main__':
    p = Person('alison', 40)
    print(p)
    d = object2dict(p)
    print(d)
    o = dict2object(d)
    # print(o.__dict__)
    # print(o)
    # print(type(o))
    # print(dir(o))

    dump = json.dumps(p, default=object2dict, sort_keys=True, indent=4)
    print(dump)
    load = json.loads(dump, object_hook=dict2object)
    print(load)
