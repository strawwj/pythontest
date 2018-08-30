#coding:utf-8
import re
dic = {}
l = []
with open("access_log-20180806") as f:
    s = f.readlines()
r1 = r'''(?P<remote_host>.*?)\s+\S+\s+\S+\s+\[.*?\] ".*?" (?P<status>[0-9]{0,}) (?P<bytes_send>[0-9-\s]{0,} (?=".*?"))'''
for i in s:
    #print(i)
    a = re.match(r1,i,re.S)
    #print(a)
    a1 = a.groupdict()
    dic.setdefault(a1['remote_host'],l).append(a1['bytes_send'])
    y = sum(int(i) for i in l if i != '- ')
print(y)
    
print(dic)
   
    
