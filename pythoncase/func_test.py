'''
输入一个数字得出绝对值
'''
def abs1(x):
    if x>0:
        return x
    else:
        return -x
a = -2
print(abs1(a))



def num_input(x):
    return x * 100
s  = 3
print(num_input(s))

'''
定义一个函数，给一个字符串，得出字符串长度
'''
def my_len(s):
    n = 0
    for i in s:
        n += 1
    return n
str1 = 'diefewgbregeu'
print(my_len(str1))
'''
形参，实参，关键字传参
'''
def func1(x,y="香草",*args,**kwargs):
    print("你好，要一个{}元的{}冰淇淋".format(x,y))
if __name__ == '__main__':
   func1(2,"nai")
   func1(x = 10,y = "巧克力",z = 12)
   f2 = (5,"草莓")
   f3 = {"x":10,"y":"抹茶"}
   func1(*f2)
   func1(**f3)
'''
用户随机输入一个数字生成数字密码
'''
import random
def my_code(n):
    code= [] 
    for i in range(1,n+1):
        c =  random.randint(0,9)
        code.append(c)
    return code
print(my_code(6))

