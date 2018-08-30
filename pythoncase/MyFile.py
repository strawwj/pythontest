#coding:utf-8
class MyOpen():
    def __init__(self,files,mod):
        try:
            f = open(files,mod)
            print("start")
        except FileNotFoundError:
            print("没有此文件")
    def __del__(self):#析构函数
        try: 
            f.close()
        except NameError:
            pass
        print("end")
f1 = MyOpen("KMSWHS.txt","r")


