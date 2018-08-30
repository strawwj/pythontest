#coding:utf-8
'''
用户输入一串字符，查看是否有f,r,i,e,n,d,拼接打印到屏幕上
'''
user = input()
a = user.find('f')
b = user.find('r')
c = user.find('i')
d = user.find('e')
e = user.find('n')
f = user.find('d')
user.find('f',user.find("f")+1)
user.find('r',user.find("r")+1)
user.find('i',user.find("i")+1)
user.find('e',user.find("e")+1)
user.find('n',user.find("n")+1)
user.find('t',user.find("t")+1)
new = (user[a]+user[b]+user[c]+user[d]+user[e]+user[f])
print(new)
'''2.将bad luck 替换成 good luck
'''
newuser = user.replace("bad","good")
print(newuser)
import random
import string
ip = '192.168.1.3'
print(ip.split('.'))


'''
从ascii码中随机选出四个
'''
import string
import random 
import random
a = []
a1 = string.ascii_uppercase
a2 = string.ascii_lowercase
a3 = string.digits
a.append(random.choice(a1))
a.append(random.choice(a2))
a.append(random.choice(a3))
a.append(random.choice(a1+a2+a3))
print(a)
'''
格式化输出256的二进制，十进制，八进制，十六进制
'''
bin(256)
int(256)
oct(256)
hex(256)
''' 
 s= We are FAMAIL",求得对应的全部大写，全部小写，以及将其切分按空格
'''
s = "We are FAMAIL"
print(str.upper(s))
print(str.lower(s))
print(s.split(" "))
'''
用户输入任意一个年份，判断有多少天
'''
year = int(input("请输入任意一年"))
if(year%4== 0 and year % 100 != 0) or year % 400 == 0:
	print("366")
else:
    print("365")

'''
要求用户输入1～100之间的整型数，如果用户输出符合要求则输出"你好棒阿！继续努力"，
否则输出"乖乖，你咋这么不听话呢"
'''
num = input("请输入1～100之间的整型数：")
e = print(num)
if (1<num<100 type(e)==int ):
	print("你好棒阿！继续努力")
else:
	print("乖乖，你咋这么不听话呢")
    

