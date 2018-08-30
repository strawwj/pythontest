#coding:utf-8
'''
1.清理指定目录下所有后缀名为.tmp的文件
'''
import os
def list_file(n):
    l = os.listdir(n)
    for i in l:
        s = os.path.join(n,i)
        if os.path.isdir(i):
            if ".tmp" in s:
                os.rmdir(s)
            else:
                list_file(s)
        else:
            os.path.isfile(i)
            if ".tmp" in s:
                os.remove(s)
            else:
                print(s)
list_file("/root")

'''
2.简易杀毒软件
假设病毒特征是文件内容含有milo字符串
'''
import os
#import sys
def f(n):
    l = os.listdir(n)
    for i in l:
        print(i)
        if os.path.isfile(i):
            with open("{}".format(i)) as k:
                k.seek(0,0)
                k = k.readlines()
                k = str(k)
                if "milomilomilo" in k:
                    os.remove(i)
                    print(i)
f("/home")

