#coding:utf-8
import subprocess
def get_Text():
    subprocess.call('ls -al',shell=True,stdout=open('a.txt','w'))
    with open('a.txt') as f:
        n = f.readlines()
    for i in range(1,len(n)):
        n1 = n[i].split( )[4]
        #print(n1)
        global n2
        global n3
        n2 = n[i].split( )[-1]
        n3 = 5120
        if int(n1)> n3:
            print('{}+ {}'.format(n1,n2))
def splitfile(sizelimit):
    size= 0
    i = 1
    out = open("access_log-20180806{}".format(i),'w')
    for line in open('access_log-20180806'):
        size=size + 1
        size+len(line)
        if(size>sizelimit):
            out.close()
            i += 1
            out=open('access_log-20180806{}'.format(i),'w')
        out.write(line)
    out.close()
get_Text()
splitfile(n3)
