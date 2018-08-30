#coding:utf-8
'''
1.请利用@property为一个Screen类实例加上width和height的获取和设置属性，在定义一个可以获取分辨率的方法
'''
class Screen():
    @property
    def x(self):
        return "长:{},宽：{}".format(self.height,self.width)
    @x.setter
    def x(self,value):
        self.width = value[1]
        self.height = value[0]
    def disg(self):
        dist =(" {} * {}".format(self.height,self.width))
        return dist
s = Screen()
s.x = 1080,1100
print(s.disg())

'''
2.定义一个直线类(Line)和点类(Point),提供一个方法getLength方法
，获取直线的长度
'''
import math
class Line():
    def __init__(self,length):
        self.length = length
    def getLength(self):
        return self.length
class Point(Line):
    def location(self,x,y):
        self.x = x
        self.y = y 
        return self.x, self.y
    def getLength(self,other):
        d =math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
        return d
if __name__ =="__main__":
    p1 = Point(1)
    p1.location(1,2)
    p2 = Point(1)
    p2.location(3,2)
    print(p1.getLength(p2))
'''
3.定义一个学生类，属性：姓名，年龄，成绩(语文，数学，英语)
方法：
    1.获取学生的姓名
    2.获取年龄
    3.三门成绩的最高分
'''
class Student():
   name = ""
   age = 0
   grade = ""
   def getName(self):
        return self.name
   def getAge(self):
        return self.age
   def gradeMax(self):
       l = self.grade.split(" ")
       m = max(l)
       return m
s = Student()
s.name = "dada"
s.age = 18
s.grade = "99 89 91"
print(s.getName())
print(s.getAge())
print(s.gradeMax())

'''
4.定义一个列表操作类：Listinfo
1)方法：
     1.列表元素的添加(添加的元素必须是字符串或者是整型数如果不是则抛出
异常)
     2.取值
     3.合并
     4.删除并返回最后一个元素
'''
class Listinfo():
    l = []
    def append1(self,value):
        self.value = value
        if type(self.value) == int or type(self.value)== str:
            self.l.append(self.value)
            return self.l
        else:
            raise TypeError ("只允许字符串和整数型的")
             
    def getValue(self,i):#根据索引获取值
        return self.l[i]
    def merge(self,other):#合并两个列表
        self.other = other
        self.l.extend(other)
        return self.l
    def del1(self):#删除最后一个并返回删除后列表的最后一个值
        self.l.pop()
        return self.l[-1] 
    
if __name__ == "__main__":        
    l1 = Listinfo()
    l2 = Listinfo()
    l1.l = [1,2,2]
    l2.l = ["aksa",1,2]
    print(l2.l)
    #print(l1.append1(12))
    print(l1.getValue(2))
    print(l1.merge(l2.l))
    print(l1.del1())
'''
5.根据字典的特性模拟一个通讯录，完成以下功能，用户根据输入的数选择功能
1.查找号码
2.增加联系人
3.删除联系人
4.修改联系人的电话号码
5.退出通讯录，并将所有联系人写入文件后的格式为
例如：张三 123442
      李四 244243
'''
class AddressList():
    d = {}
    def seach(self,name):#根据姓名查找电话号码
        return "{} {}".format(name , self.d[name])
    def add(self,x,y):#添加新的联系人
        self.x = x
        self.y = y
        self.d[x] = y
        with open("address_list.txt","a+") as f:
            s = "{} {}".format(self.x, self.y)
            f.writelines(s)
        return self.d
    def del1(self,name):#根据名字删除联系人
         self.d.pop(name)
         return self.d
    def change(self,name,other):#根据名字更改电话号码
        self.d[name]= other
        return "{} {}".format(name , self.d[name])
if __name__ == "__main__":
    a1 = AddressList()
    a2 = AddressList()
    a1.d = {"wj":12324354}
    a2.d = {"wqi":123243}
    print(a1.seach("wj"))
    print(a1.add("wy",123243))
    a2.add("ww",20130291)
    print(a1.del1("wy"))
    print(a1.change("wj",13572468))
