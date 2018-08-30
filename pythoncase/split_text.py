#coding:utf-8
import subprocess
import re
from threading import Thread
l = []
def get_Text():
    subprocess.call('ls -al',shell=True,stdout=open('a.txt','w'))
    with open('a.txt') as f:
        n = f.readlines()
    for i in range(1,len(n)):
        n1 = n[i].split( )[4] #n1 为得到文件的大小
        #print(n1)
        global n2    #n2 为文件的名字
        n4 = n[i].split()[0]
        n5 = re.findall(r'^(-).*?',n4)  #n5得到是文件还是目录
        #print(n5)
        #print(n4)
        n2 = n[i].split( )[-1]
        n3 = 10240   #指定以多少为切割
        if int(n1)> n3 and n5 == ['-']:
            l.append(n2)
            #print(l)
            print('{}+ {}'.format(n1,n2))
def splitfile():
    for i in l:
        with open("{}".format(i),'rb') as out:
            while True:
                out1 = out.read(1024)
                if out1:
                    with open('copy_{}'.format(i),'ab') as save:
                          save.write(out1)
                else:
                    break
get_Text()
for j in range(10):
    t = Thread(target= splitfile)
    t.start()            
