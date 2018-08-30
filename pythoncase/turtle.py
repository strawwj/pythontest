import random as rd
def move(i, x, y):
    for v in range(1,i+1):
        b = rd.randint(1,4)
        if b == 1:
            if x+1 <= 10:
               x = x + 1
            else:
                v -= 1
        elif b == 2:
            if x-1 >= 0:
                x = x - 1
            else:
                v -= 1
        elif b == 3:
            if y+1 <= 10:
                y = y + 1
            else:
                v -= 1
        return [x,y]
class animal():

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.a=[self.x,self.y]
    def run(self):
        a = rd.randint(1,2)
       # for i in range(a):
        if self.x=='die' or self.y=='die':
            pass
        else:
            b=move(a,self.x,self.y)
            self.tili -= 1
            self.a = b
    def where_is(self):
        return self.a
    def life(self):
        if self.tili <= 0:
            self.x='die'
            self.y='die'
            self.a=[self.x,self.y]
    @property
    def say(self):
        return '¿¿¿'

class turhan(animal):

    def __init__(self,x=5,y=5):
        self.x = x
        self.y = y
        self.tili=100
        self.a=[self.x,self.y]
    def run(self):
        a = rd.randint(1,2)
       # for i in range(a):
        if self.x=='go die' or self.y=='go die':
            pass
        else:
            b=move(a,self.x,self.y)
            self.tili -= 1
            self.a = b
    def whereT(self):
        return self.a
    def life(self):
        if self.tili <= 0:
            print('¿¿¿¿')
            self.x='go die'
            self.y='go die'
            self.a=[self.x,self.y]
        else:
            return self.tili
    def eat(self):
        self.tili+=10
    @property
    def say(self):
        return '¿¿¿¿¿¿¿¿¿¿¿'

class fish(animal):
    def __init__(self,x=rd.randint(1,10),y=rd.randint(1,10)):
        self.x=x
        self.y=y
        self.a=[self.x,self.y]
    def run(self):

        if self.x=='' or self.y=='':
            pass
        else:
            b=move(1, self.x, self.y)
            self.a=b
    def whereF(self):
        return self.a
    def die(self):
        self.x = ''
        self.y = ''
        self.a = [self.x, self.y]

    @property
    def laugh(self):
        return '¿¿¿¿¿¿'


