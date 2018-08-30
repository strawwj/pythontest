#coding:utf-8
l = []
for i in range(1,10):
    if (i % 3 == 0 or i % 5 == 0):
         l.append(i)
print(l)
print(sum(l))




print([i for i in range(1,10) if i%3==0 or i%5==0])
g = (i for i in range(1,10) if i%3==0 or i%5==0)
print(type(g))
print(g)



print([i for i in range(1,101) if i%2==0])
print([10 * i for i in range(1,101) if i%2==0])
'''
随机产生100以内的100个整型数值，存储在一个列表中，统计有多少个偶数
'''
import random 
count = 0
num = []
for i in range(1,101):
    num.append(random.randint(1,101))
for i in num:
    if i%2 == 0:
        print(i)
        count += 1
print(count)


'''
求得100以内的所有偶数序列中有多少个是5的倍数
'''
count1 = 0
l1 = []
for i in range(1,101):
    if i%2== 0:
        l1.append(i)
print(l1)
for i in l1:
    if i%5== 0:
        count1 += 1
print(count1)


'''
用户输入10个人的名字，随机选取一个人作为队长
'''
#duizhang = []
user_input = list(input("输入十个人名："))
print(user_input)
duizhang = random.choice(user_input)
print(duizhang)

'''
不使用python的sort方法，为列表排序

stu = ['2','4','6','1','7']
for i in range(3):
    for i in range(len(stu)-1):
        if stu[i]> stu[i+1]:
            stu[i],stu[i+1]= stu[i+1],stu[i]
        print(stu)    
'''

stu = [2,34,56,12,45]
flag = True
while flag:
    flag = False
    for i in range(len(stu)-1):
        if stu[i]> stu[i+1]:
            stu[i],stu[i+1]= stu[i+1],stu[i]
            flag = True
            print(stu)
    #print(stu)    
    
