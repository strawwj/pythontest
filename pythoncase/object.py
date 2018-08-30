#coding:utf-8
def hero(name,hp):
    data = {"name":name, "hp":hp}
    return data
def ak(player):
    print("{} kill boss".format(player))
milo = hero("milo",100)
w = hero("w",200)
ak("milo")
ak("w")
print(milo["name"])

def monster(name,hp):
    data = {"name":name,"hp":hp}
    return data
milo = hero('milo',100)
turtle = monster("turtle", 900)
ak(milo)

'''
类
'''
class Ren():
 #属性须有默认值
    name = ''
    age = ''
    money = ''
    def say(self):
        print("hello! i am {}".format(self.name))
#对象的实力化，可以调用类的属性和方法say方法只有对象可以调用
zhangsan = Ren()
lisi = Ren()
zhangsan.name = "zhangsan"
zhangsan.age = 20
zhangsan.money = 1000
print("i am {} i have {} yuan!".format(zhangsan.name, zhangsan.money))
zhangsan.say()

'''
打印机类
'''
class DaYinJi():
    color = 'white'
    size = ''
    type1 = "黑白"    
    def daYin(self):
        if self.type1 == "黑白":
            print("{}打印机能打印黑白字".format(self.type1))
        elif self.type1 == "彩色":
            print("{}打印机能打印照片".format(self.type1))
        else:
            print("不支持此类")
d1 = DaYinJi()
d2 = DaYinJi()
d1.type1 = "黑白"
d1.color = "white"
d1.size = "small"
d2.color = "whitle"
d2.size = "big"
d2.type1 = "彩色"
d1.daYin()

#d2.say()


'''
矩形类
属性：长和宽
方法：设置长和宽
      获取长和宽
      获取面积
'''
class JuXing():
    '''
    this is a class of JuXing
    '''
    __length = 0
    __width = 0
    def mianJi(self):
        s = self.__length * self.__width 
        return s
    def zhouChang(self):
        return 2*(self.__length + self.__width)
    def panDuan(self):
        if self.__length == self.__width:
            print("是个正方形")
        else:
            print("是个矩形")
    def setside(self,x,y): #设置一个值不需要返回值
        self.__length = x
        self.__width = y
    def getside(self): #获取返回的值
        return self.__length
        return self.__width
if __name__ == "main":
    j1 = JuXing()
    j1.length = 12
    j1.width = 4
    print(j1.mianJi())
    j2 = JuXing()
    j2.setside(10,5)
    print(j2.mianJi())
    print(j2.getside())
    print(j1.length)
    j3 = JuXing()
    j3.setLength(10,10)
    print(j3.mianJi())
    print(j3.zhouChang())
    j3.panDuan()
    print(j3.__doc__)
'''
初始化长宽为私有属性，求面积
'''
class ChangFangXing():
    def __init__(self,length,width):
        self.__length = length
        self.__width = width
    def area(self):
        return self.__length * self.__width
if __name__ == "__main__":
    s1 = ChangFangXing(3,4)
    s2 = ChangFangXing(4,5)
    print(s1.area()) 
    print(s2.area())

'''
定义一个北京欢乐谷门票类，计算两个社会青年和一个学生平时比
节假日门票能省多少钱
票价是除节假日100/天
节假日为平时的1.2倍
学
'''
'''
定义一个三角形的类
'''
import math
class Triangle():
    
    #class Triangle()--> return a Trangle object
    
    __bian1 = 0
    __bian2 = 0
    __bian3 = 0
    def getBian(self):
        return self.__bian1,self.__bian2,self.__bian3
    def setBian(self,bian1,bian2,bian3):
        self.__bian1 = bian1
        self.__bian2 = bian2
        self.__bian3 = bian3
        self.judge()
    def judge(self):
        if not (self.__bian1+self.__bian2>self.__bian3 and self.__bian2+self.__bian3>self.__bian1 and self.__bian1+self.__bian3>self.__bian2):
            raise TypeError('不构成三角形')
        else:
            print("是三角形")
    def area(self,a,b,c):
        self.__bian1 = a
        self.__bian2 = b
        self.__bian3 = c
        p = (a+b+c)/2
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        return float(s)
if __name__ == "__main__":
    t1 = Triangle()
    t2 = Triangle()
    t1.setBian(3,4,5)
    print(t2.area(3,4,5))
    #print(t1.getBian())
    #t2.setBian(1,2,3)

