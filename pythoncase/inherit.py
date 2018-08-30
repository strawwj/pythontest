#coding:utf-8
import math
class Shape():
    def __init__(self,length,width,radius = 3):
        self.__length = length
        self.__width = width
        self.__radius = radius
    def area(self):
        s = self.__length * self.__width
        return s
    def perimeter(self):
        p = (self.__length + self.__width)*2
        return p
class Rectangle(Shape):
    pass
class Circle(Shape):
    radius = 0
    def area(self,radius):
        s = 3.14 * (radius**2)
        return s
    def perimeter(self,radius):
        p = 2*3.14*radius
        return p
class Triangle(Shape):
    def __init__(self,x,y,z):
        self.__x = x
        self.__y = y
        self.__z = z
    def area(self,x,y,z):
        p = (self.__x +self.__y+self.__z)/2
        s = math.sqrt(p*(p-x)*(p-z)*(p-y))
        return s
    def perimeter(self,x,y,z):
        p = self.__x+self.__y+self.__z
        return p 
if __name__ == "__main__":
    r1 = Rectangle(3,4,5)
    r2 = Circle(3,4,5)
    r3 = Triangle(3,4,5)
    print(r1.area())
    print(r2.area(3))
    print(r3.area(3,4,5))
    print(r1.perimeter())
    print(r2.perimeter(4))
    print(r3.perimeter(3,4,5))
'''
封装一个文件操作的类(用open)，初始化时获取文件操作对象，提供读取文件并加行号显示的
加行号通过字典
'''
class FileOperate():
    def __init__(self,files):
        self.files = files
        print("文件是{}".format(self.files))
    def openFile(self):
        dic = {}
        f =  open ("{}".format(self.files),"a+")
        f.seek(0,0)
        d = f.readlines()
        for j in range(1,len(d)+1):
            dic[j] = j
            for i in d:
                dic[j]= i            
        return dic
        def __del__(self):
            self.openFile()
            f.close()
f1 = FileOperate("KMSWHS.txt")
print(f1.openFile())

