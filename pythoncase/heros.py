#!/usr/bin/python
#coding:utf-8
import os
select = input("1 for login |  2 for regist:")
if select =="1":
    for i in range(3):
        username = input("your name:")
        passwd1 = input("your passwd:")
        if not os.path.exists("{}.lock".format(username)):
            with open("passwd.db") as p:
                allline = p.readlines()
                for line in allline:
                    upl = line.split("-+ -")
                    #print(upl)
                    if username == upl[0]and passwd1== upl[1].strip():
                         print("welcome!")
            break
        else:
            print("user {} is locked!".format(username))
    else:
        with open("{}.lock".format(username),"w") as f:
            pass
elif select == '2':
    username = input("your name")
    passwd1 = input("your passwd1:")
    passwd2 = input("your passwd2:")
    if passwd1 == passwd2:
        with open("passwd.db","a+") as p:
            p.write(username+ "-+ -"+ passwd1+'\n')

