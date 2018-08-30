import random
init_x = [0,10]
init_y = [0,10]
class Turtle:
    def __init__(self):
        self._x = random.randint(init_x[0],init_x[1])
        self._y = random.randint(init_y[0],init_y[1])
        self.hp = 100
    def move(self):
        newx = self._x + random.choice([1,2,0,-1,-2]) 
        newy = self._y + random.choice([1,2,0,-1,-2])
        if newx>10:
            self._x = self._x-(newx -init_x[1]) 
        elif newx<0:

