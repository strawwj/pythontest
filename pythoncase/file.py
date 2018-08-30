#coding:utf-8
'''
根据绝对路径查找路径下的目录与文件
'''
import os
import sys
def list_dir(path):
    file_name_list = os.listdir(path)
    for file_name in file_name_list:
        file_path_name = os.path.join(path,file_name)
        if os.path.isfile(file_path_name):
            print(file_path_name)
        else:
            list_dir(file_path_name)
list_dir(sys.argv[1])
