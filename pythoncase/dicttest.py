#coding:utf-8
#方法一
s = 'qwertyuipoiuytre'
t = {}
for i in s:
    c = 0
    for j in s:
        if i == j:
            c += 1
            t[i]= c
print(t)

#方法二
s = 'qwertyuipoiuytre'
d = {}
for i in s:
    if i in d:
        d[i]+= 1
    else:
        d[i] = 1
print(d)


'''
现在有一个列表，li = [1,2,3,'a','b','4','c'] dic = {}如果字典没有k1这个键，创建此键并将列表li中索引为奇数的内容添加到k1中
'''
li = [1, 2, 3, 'a', 'b', '4', 'c']
dic = {}
dic["k1"]= li[0::2]
print(dic)

'''
组合嵌套
lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
1.将列表lis中的'tt'变成大写(两种方式)
2.将列表lis中数字3变成字符串'100'(两种方式)
3.将列表中'1'变成数字101(两种方式)
'''
lis = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]
l = lis[0][1][2]["k1"][0].upper()
l1 = str(lis[0][1][2]["k1"][1]).replace('3','100')
l2 = lis[0][1][2]["k1"][2].replace('1', '101')
print(l,l1,int(l2))
        
'''
请删除字典中的键k5，如果不存在k5，则输出"对不起！不存在你要的删除元素"
'''
'''
dir1 = {"k1":"wj","k2":"wy","k5":"wq"}
for k in dir1:
    if k == "k5":
        del(dir1[k])
        print(dir1)
else:
    print("对不起！不存在你要删除的元素")
''' 
'''
统计文本文件"kmswhs.txt"中所有的单词出现的频率，将排在前十的单词以漂亮的形式打印出来
'''
dic = {}
dic1 = []
with open("KMSWHS.txt","a+") as f:
    f.seek(0,0)
    f.flush()
    f = f.readlines()
    f = str(f)
    for i in f.split(" "):
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
print(dic)
dic = sorted(dic.items(),key = lambda x:x[1],reverse = True)
for i in dic:
    dic1.append(i)
    if i == dic[9]:
        break
print(dic1)
o =  open("wordcloud1.txt","w+")
o.writelines(str(dic1))
o.close()

