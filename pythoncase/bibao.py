'''
闭包：在函数中定义一个函数，这个函数返回一个新定义的函数
'''
def greeting_conf(prefix):
    def greeting(name):
        print(prefix,name)
    return greeting
mGreeting = greeting_conf("Good Morning")
print("function name is:",mGreeting.__name__)
print("id of mGreeting is:",id(mGreeting))
mGreeting("Willer")
mGreeting("Will")
aGreeting = greeting_conf("Good Afternoon")
print("function name is:",aGreeting.__name__)
print("id of aGreeting is:",id(aGreeting))
aGreeting("Willer")
aGreeting("Will")
'''
例2
'''
def f(prefix):
    def inner(name):
        print("{}-->inner-->{}".format(prefix,name))
    return inner
morning = f("Morning")
print("morning function name:{}".format(morning.__name__))
print("morning function id:{}".format(id(morning)))
afternoon = f("Morning")
print("afternoon function name:{}".format(afternoon.__name__))
print("afternoon function id:{}".format(id(afternoon)))

'''
装饰器
'''
import time
def deco(fun):
    def inner():
        start_time = time.time()
        fun()
        ended_time = time.time()
        print((ended_time-start_time)*1000)
    return inner

def f():
    for i in range(1000):
        pass
def ff():
    for i in range(10):
        print("ff")
def my_func():
    print("starting myfunc")
    time.sleep(1)
    print("ended myfunc")
my_func = deco(my_func)
my_func()
'''
例2
'''
def deco(func):
    def wrapper():
        startTime = time.time()
        func()
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("->elapsed time:%f ms"%msecs)
    return wrapper
def myfunc():
    print("start myfunc")
    time.sleep(0.6) 
    print("end myfunc")
print("myfunc is:",myfunc.__name__)
myfunc = deco(myfunc)
print("myfunc is :",myfunc.__name__)
myfunc()
'''
装饰语法糖@
'''
@deco
def ff():
    for i in range(4):
        print("ff")
def my_func1():
    print("starting myfunc")
    time.sleep(5)
    print("ended myfunc")
ff()
