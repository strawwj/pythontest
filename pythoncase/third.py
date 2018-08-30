#coding:utf-8
num = int(input("请输入一个整型数："))
if (num % 2==0):   
    print("{}是一个偶数".format(num))
else:
    print("{}是一个奇数".format(num))


'''
用户输入一个字符串，如果字符串中有大写，则全部转换为小写，否则全部转换为大写
'''
import string
str1 = input("请输入一个字符串：")
if (str1.islower()):
    print(str.upper(str1))
else:
    print(str.lower(str1))
'''
找到1～100相加
'''
n = 0
for i in range(1,101):
    n = n + i
print(n)

'''
100以内3，5的倍数之和
'''

l = []
s = 0
for i in range(1,100):
	if (i % 3 == 0 or i % 5 == 0):
		#print(i)
		s = s + i
		l.append(s)
print(s)
print(l)	


''' 
连续整数之和,和能被操作数整除，显示和的值
'''
x = 0 
num = int(input("输入一个整数:"))
for i in range(1,num+1):
	#print(i)    
	x = x + i 
	# print(x)
	if (x % num == 0 ):
		print("和为{}".format(x))
		continue   

'''
以循环嵌套实现连续整数和

x = 0
num = int(input("输入一个整数："))
for i in range(1,num+1):
    print(1 = 1)
		#for j in range(2,num+1):
            i1= print("1+2")
            i2=i1+num
'''   
'''
任意输入一个正整数，判断其是否为质数
'''
import math
n = int(input("请输入一个正整数："))
n1 = math.sqrt(n)
for i in range(2,int(n1)):
    if n % i == 0:
        print("{}不是质数".format(n))
        break
else:
    print("{}是质数".format(n))

'''
求得1～100之间有多少个质数
'''
import math
count = 0
for i in range(1,101):
    for j in range(2,int(math.sqrt(i)+1)):
        if i % j == 0:
            break
    else:
        count += 1
        print(i)
print(count)

      
'''
计时器，将计时时间显示出来
'''		
import time
t1 = time.time()
t2 = time.time()
t3 = t2 - t1
print(t3)

'''
读入行数，输出以下形状
'''
h = int(input("输入一个行数："))
n = '* '
for i in range(1,h+1):
    print(i * n)

'''
输出形状2.0
'''
a = ' '
n = "* "
for i in range(1,6):
    a1 = ((-i)+ 6)*a
    n1 = i * n
    print(a1+n1)

    
