#coding:utf-8
import re
import sys
def my_Re():
    count = 0
    count1= 0
    r1 = r'(?<=def) [a-zA-Z_]\w*\(.*?\)(?=:)'
    r2 = r'\b[a-zA-Z_]\w*(?=\s?=)'
    r3 = r'(?<=for) \b[a-zA-Z_]\w*(?=in)'
    with open("{}".format(sys.argv[1]),"r") as f:
        all_lines = f.readlines()
    print('###############################')
    print('{}中的函数有：'.format(sys.argv[1]))
    print('###############################')
    for i in all_lines:
        #print(i)
        count += 1
        re1 = re.findall(r1,i,re.M)
        if re1 != []:
            print('第{}行：{}'.format(count,re1))
    print('###############################')
    print('{}中的变量有：'.format(sys.argv[1]))
    print('###############################')
    for i in all_lines:
        count1 += 1
        re2 = re.findall(r2,i,re.M)
        re3 = re.findall(r3,i,re.M)
        if re2 != []:
            print('第{}行：{}'.format(count1,re2))
        elif re3 != []:
            print('第{}行：{}'.format(count1,re3))
            
my_Re()

