class Hero():
    '''this is game heros'''
    def __init__(self,name = 'player01',hp= 100,ack= 10):
        self.name = name
        self.hp = hp
        self.ack = ack
    def say(self):
        return "superman!!!"
    def ack(self):
        y = self.ack-10
        return y
    def getHP(self,x = 'baozi'):
        self.x = x
        if self.x == "baozi":
            self.hp += 10
        else:
            pass
    def ackkk(self,other):
        other.hp -=self.ack
        print("{}打了{}一下 造成伤害{}".format(self.name,other.name,self.ack))
        return other.hp
        
class Boss():
    def __init__(self,name='Turtle',hp=60,ack=20):
        self.name = name
        self.hp = hp
        self.ack = ack
    def say(self,x):
        return x
        
