'''
多态
'''
class Ren():
    @classmethod #类方法
    def say(self):
        print("i am a person")
class Man(Ren):
    @staticmethod #静态类方法只有类可以用不需要self
    def say():
        print("i am a man")
class Woman(Ren):
    def say(self):
        print("i am a woman")
class Baby(Man,Woman):
    pass
def f(x):#通过一个函数调用不同类的同一方法
    x.say()
f(Ren())
r = Ren()
Ren.say()
m = Man()
r.say()
m.say()
#instance()
class Person():
    def __init__(self,f = "zhang",l = "san"):
        self.l = l
        self.f = f
    @property #属性方法把方法变成一个变量
    def full_name(self):
        return "{},{}".format(self.f,self.l)
    @full_name.setter
    def full_name(self,value):
        self.value = value.split(" ")
        self.f= self.value[0]
        self.l = self.value[1]
#zhangsan = Person("zhang","san")
#print(zhangsan.full_name[0:5])
#zhangsan = Person("zhang","san")
li = Person()
li.full_name = "zhang sansan"
print(li.full_name)
'''
'''
class Fees():
    def __init__(self):
        self.__fee = None
    def get__fee(self):
        return self.__fee
    def set__fee(self,value):
        self.__fee = value
    fee = property(get__fee,set__fee)
f = Fees()
#print(f.get__fee())
f.set__fee(11)
print(f.get__fee())
print(f.fee)
f.fee = 22
print(f.fee)





'''
经典类: 父类.方法(self)  先左后右 深度调用
DBAABCAACD
'''
class A():
    def __init__(self):
        print("enter A")
        print("leave A")
class B(A):
    def __init__(self):
        print("enter B")
        A.__init__(self)
        print("leave B")
class C(A):
    def __init__(self):
        print("enter C")
        A.__init__(self)
        print("leave C")
class D(B,C):
    def __init__(self):
        print("enter D")
        B.__init__(self)
        C.__init__(self)
        print("leave D")
d = D()
'''
新式类：super(当前类，self) 层次调用
DBCAACBD
'''
class A():
    def __init__(self):
        print("enter A")
        print("leave A")
class B(A):
    def __init__(self):
        print("enter B")
        super(B,self).__init__()
        print("leave B")
class C(A):
    def __init__(self):
        print("enter C")
        super(C,self).__init__()
        print("leave C")
class D(C,B):
    def __init__(self):
        print("enter D")
        super(D,self).__init__()
        print("leave D")
d = D()
