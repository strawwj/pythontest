class A():
    name = "A class"
    def a(self):
        print("i am {}".format(self.name))
class B(A):#继承A类
    pass
if __name__ == "__main__":
    a1 = A()
    a1.a()
    b1 = B()
    print(b1.name)
    b1.a()

'''
'''
class Father():
    first_name = "wang"
    last_name = "xizhi"
    __money = 1000
    def say(self):
        print("i am {}{},i have{}".format(self.first_name,self.last_name,self.__money))
    def __lie(self):
        print("lie")
class Mother():
    __money = 5000
    first_name = "wang"
    last_name = "shi"
    def run(self):
        print("i can run!!")
class Son(Father,Mother):
     last_name = "xianzhi"
     __money = 1000000
     other = "i can fly!"
     def say(self):
        print("i am {}{},i have {}".format(self.first_name,self.last_name,self.__money))
        print("my father is {}{}".format(Father.first_name,Father.last_name))
wangxianzhi = Son()
wangxianzhi.say()
wangxianzhi.run()
'''
重载运算符
'''
class MyList():
    __mylist = []
    def __init__(self,*args):
        self.__mylist = [i for i in args]
    def __add__(self,x):
        '''
        list中的每个值加上x
        '''
        return [i+x for i in self.__mylist]
    def __sub__(self,x):
        return [i-x for i in self.__mylist]
    def __mul__(self, x):
        return [i*x for i in self.__mylist]
    def __truediv__(self,x):
        return [i/x for i in self.__mylist]
    def show(self):
        print(self.__mylist)
    def __del__(self):#魔术方法清除
        print("defrge")
l = MyList(1,2,4,5)
l.show()
print(l+10)
print(l-1)
print(l*2)
print(l/2)
print("aaaa")
