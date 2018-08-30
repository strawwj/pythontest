#coding:utf-8
'''
随机产生一个正整数，求得二进制并输出
'''
import random
n = random.randint(1,100)
print(n)
l = []
while True:
    if n == 0 or n == 1:
        l.append(n)
        break
    else:
        n1 = n % 2
        n = n // 2
        if n1 == 0:
            l.append(0)
            continue
        elif n1 % 2 == 1:
            l.append(1)
            continue
l.reverse()
print(l)


'''
删除元组中所有重复的元素，并生成一个列表
'''
t = (1,2, 3, 1, 2, 3, 4, 5)
l = list(t)
l.sort()
for i in l:
    if l[i-2]== l[i-1]:
        l.remove(l[i-1])
        print(l)
print(l)

