'''
1.定义一个函数，可以返回用户设定位数的随机密码，数字密码
'''
import random
def user_code():
    l = []
    n = int(input("请输入一个整数："))
    for i in range(1,n+1):
        code = random.randint(0,9)
        #print(code)
        l.append(code)
    print(l)
user_code()


'''
2.做一个点名软件，每次随机打印名字
''' 
def roll_book():
    import random
    classmate = ["王凯","王浩然","赵晗","吴静","周金玲","潘非","马青峰","李东鹤","王帅","郭旭炜","刘佳琪","陈天博","信欣","路钦","高福根","王铭","安雨琪","李松郁","雷梦祥","张学磊","郑慧东","马佳琪","焦志豪","惠佳运","刘金盛","王东"]
    lucky = random.choice(classmate)
    return lucky
print(roll_book())
'''
3.计算l = ["172.16.3.1","172.16.1.5","172.15.2.0","172.16.3.1","172.16.3.1","172.16.1.5"]
不需要定义函数，统计在此列表中每一个ip出现的次数，并输出频率最高的成员
'''
dic = {}
l = ["172.16.3.1","172.16.1.5","172.15.2.0","172.16.3.1","172.16.3.1","172.16.1.5"]
for i in l:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)
sorted(dic.items(),key = lambda x:x[1],reverse = True)
for i in dic:
    print(i,dic[i])
    break

'''
4.定义一个函数，计算给定的整形数是否为质数
'''
import math
def prime_num():
    n = int(input("请输入一个整数："))
    n1 = int(math.sqrt(n))
    for i in range(2,n1+1):
        if n% n1== 0:
            print("{}不是一个质数".format(n))
            break
    else:
        print("{}是一个质数".format(n))
prime_num()

'''
5.定义一个函数，完成以下功能：
1）输入两个整型数，例如输入的是3，5 此函数要计算的是3 + 33 + 333 + 3333 + 33333（到5为止）
'''
def int_num():
    x = int(input("请输入一个整型数："))
    y = int(input("请输入一个整型数："))
    a = 0 
    a1 = 0
    for i in range(0,y):
        a = x*(10**i) + a
        a1 = a + a1
    print(a1)
int_num() 

'''
6.定义一个函数，判断用户输入的成绩所属于的等级
'''
def grade_stu(gra):
    if 90<= gra<= 100:
        return 'A'
    elif 80<= gra<= 89:
        return 'B'
    elif 70<= gra<= 79:
        return 'C'
    elif 60<= gra<= 69:
        return 'D'
    elif 0<= gra<= 59:
        return 'E'
    else:
        print("请重新输入：")
print(grade_stu(98))


'''
7.编写一个函数，计算所有参数的和的基数倍（默认基数为base = 3）
'''

'''
8.定义一个函数，判断输入的字符串是否是回文字符串 （例如上海自来水来自海上）
'''
def hui_wen(n):
    l = len(n)
    for i in range(1,int(l/2)):
       if n[i]== n[-i-1]:
           return True
       else:
           return False
print(hui_wen(n = "上海自来水来自海上"))

'''
9.编写一个函数，此函数可以传递任意一组键值对，函数将所有的键存放到一个列表中，返回
升级以上函数，使得用户必须有的键值为：name："xxx" city:"xxxxx"
'''
def dic_t(): 
    l = []
    dic = {}
    x = input("请输入一个键：")
    y = input("请输入一个值：")
    dic[x]= y
    for k in dic:
        l.append(x)
    print(dic)
    return l
print(dic_t())


'''
升级版
'''
l1 = []
def dic_t1():
    dic1= {"name":"xxx","city":"xxxx"}
    for i in dic1:
        if i == "name":
            dic1[i] = input("请输入你的名字：")
        elif i == "city":
            dic1[i] = input("请输入你的所在地：")
    x1= input("请输入一个键：")
    y1= input("请输入一个值：")
    dic1[x1] = y1
    print(dic1)
    for i in dic1:
        l1.append(i)
    return l1
print(dic_t1())
'''
10.定义一个函数，实现字符串的len方法
'''

def my_len(s):
    count = 0
    for i in s:
        count += 1
    return count
print(my_len("hello"))
