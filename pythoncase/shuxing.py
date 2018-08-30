#coding:utf-8
class Ren():
    name = ""
    age = 0
    __money = 1000  #私有属性
    def say(self):
        print("hello! i am {} i have {} yuan ".format(self.name,self.__money))
zhangsan = Ren()
zhangsan.name = "zhangsan"
zhangsan.say()
'''
私有方法
内部使用
'''
class Ren():
    name = ""
    age = 0
    __money = 1000  #私有属性
    def __say(self):
        print("hello! i am {} i have {} yuan ".format(self.name,self.__money))
    def lie(self,some = "friend"):
        if some == "wife":
            self.__say()
        else:
            print("i have 0 yuan")

zhangsan = Ren()
zhangsan.name = "zhangsan"
zhangsan.lie("wife")
'''
初始值init
'''
class Ren():
    def __init__(self,name = "",age = 0,money = 1000):
        self.name = name
        self.age = age
        self.__money = money
    def __say(self):
        print("hello! i am {} i have {} yuan ".format(self.name,self.__money))
    def lie(self,some = "friend"):
        if some == "wife":
            self.__say()
        else:
            print("i have 0 yuan")
class Baby(Ren):
    high = 100
    def cry(self):
        print('i am {} i am {},i want you money{}'.format(self.name,self.high,self.__money))
zhangsan = Ren("zhangsan",25,1000)
zhangsan.lie("wife")
lisi = Baby("lisi",1,1000)
print(lisi.name)
lisi.lie("wife")
lisi.cry()

'''
魔法方法__str__
'''
class Ren():
    def __init__(self,name,age,money):
        self.name = name
        self.age = age
        self.__money = money
    def __say(self):
        print("hello! i am {} i have {} yuan ".format(self.name,self.__money))
    def lie(self,some = "friend"):
        if some == "wife":
            self.__say()
        else:
            print("i have 0 yuan")
     def __str__(self):
         print("this is a object of Ren")
