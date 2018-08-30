#coding:utf-8
'''
问题：坐标可能不会移动，xy会同时变化，遇到0时就不会移动了
小鱼也会走两步
'''
import random
class Turtle():
    def __init__(self,name,hp,x,y):
        self.x = x
        self.y = y
        self.name = name
        self.hp = hp
    def location(self):
        direction = ["right","left","up","down"]
        self.d = random.choice(direction)
        self.r = random.randint(1,2)
        if self.d == "left" and self.r == 1:
           if  0<self.x<10:
               self.x -= 1
           elif self.x == 0:
               self.d = "right"
           elif self.x == 10:
               self.d = "left"
        elif self.d == "right" and self.r == 1:
           if  0<self.x<10:
               self.x += 1
           elif self.x == 0:
               self.d = "right"
           elif self.x == 10:
               self.d = "left"
        elif self.d == "up" and self.r == 1:
           if  0<self.y< 10:
               self.y += 1
           elif self.y == 0:
               self.d = "up"
           elif self.y == 10:
               self.d = "down"
        elif self.d == "down"and self.r == 1:
           if  0<self.y<10:
               self.y -= 1
           elif self.y == 0:
               self.d = "up"
           elif self.y == 10:
               self.d = "down"
        elif self.d == "left" and self.r == 2:
           if  1<self.x<10:
               self.x -= 2
           elif self.x == 0:
               self.d = "right"
           elif self.x == 10:
               self.d = "left"
        elif self.d == "right" and self.r == 2:
           if  0<self.x< 9:
               self.x += 2
           elif self.x == 0:
               self.d = "right"
           elif self.x == 10:
               self.d = "left"
        elif self.d == "up" and self.r == 2:
           if  0<self.y< 9:
               self.y += 2
           elif self.y == 0:
               self.d = "up"
           elif self.y == "down":
               self.d = "left"
        elif self.d == "down"and self.r == 2:
           if  1<self.y<10:
               self.y -= 2
           elif self.y == 0:
               self.d = "up"
           elif self.y == 10:
               self.d = "down"
        return self.x,self.y    
    def kill(self,other):#当位置重合，吃掉小鱼hp+10
        if self.location() == other.location():
           self.hp += 10
           print("{} killed".format(other.name),self.hp)
        else:
            print("hp还剩{}".format(self.hp))
    def reduceHp(self):#移动时hp减少，不是一直在减少还有增加的时候？？？
        self.hp -= 1
        if self.hp == 0:
            print("game over")
            print("小样！还想吃我")
        else:
            print("ph:{}".format(self.hp))
                
class Fish():
    def __init__(self,name,x,y):
        self.x = x
        self.y = y
        self.name = name
    def location(self):
        direction = ["right","left","up","down"]
        self.d1 = random.choice(direction)
        if self.d1 == "up":
           if  0<self.y<10:
               self.y += 1
           elif self.y == 0:
               self.d = "up"
           elif self.y == 10:
               self.d = "down"
        elif self.d1 == "down":
           if  0<self.y<10:
               self.y -= 1
           elif self.y == 0:
               self.d = "up"
           elif self.y == 10:
               self.d = "down"
        elif self.d1 == "left":
           if  0<self.x<10:
               self.x -= 1
           elif self.x == 0:
               self.d = "right"
           elif self.x == 10:
               self.d = "left"
        elif self.d1 == "right":
           if  0<self.x<10:
               self.x += 1
           elif self.x == 0:
               self.d = "right"
           elif self.x == 10:
               self.d = "left"
        return self.x,self.y 
if __name__ == "__main__": 
    turtle1 = Turtle("turtle1",10,1,2)
    nimo = Fish("nimo",1,4)
    print(turtle1.location())
    print(nimo.location())
    print(turtle1.kill(nimo))
    print(turtle1.hp)

