'''
遍历目录

'''

import os

#  直接使用
path = r'e:\\'
for dirpath, dirnames, filenames in os.walk(path):
    for file in filenames:
        fullpath = os.path.join(dirpath, file)
        print(fullpath)


#  封装成函数
def paths(path):
    path_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            path_collection.append(fullpath)
    return path_collection


def test01():
    for file in paths(path):
        print(file)


#  封装成类
import os, sys


class diskwalk(object):
    def __init__(self, path):
        self.path = path

    def paths(self):
        path = self.path
        path_collection = []
        for dirpath, dirnames, filenams in os.walk(path):
            for file in filenames:
                fullpath = os.path.join(dirpath, file)
                path_collection.append(fullpath)
        return path_collection


if __name__ == '__main__':
    for file in diskwalk(sys.argv[1]).paths():
        print(file)


def file_extension(path):
    return os.path.splitext(path)[1]


#  查找出磁盘中所有的文档，按照磁盘遍历出来
extension_collection = ['.doc', '.docx', '.pdf', '.xls', 'xlsx', '.pptx', '.ppt']
path_collection = ['c:\\Users\\admin\\Desktop', 'D:\\', 'E:\\']
write_file = r'c:\\users\\admin\\desktop\\20190228.log'
with open(write_file, 'a+', encoding='utf-8') as f:
    for path in path_collection:
        if path.find('c:'):
            f.write('[C]\n')
        else:
            f.write('[' + path.replace(r':\\\\', '') + ']\n')
        for dirpath, dirnames, filenames in os.walk(path):
            for file in filenames:
                if file_extension(file) in extension_collection:
                    fullpath = os.path.join(dirpath, file)
                    print(fullpath)
                    f.write('\t' + fullpath + '\n')
f.close()
