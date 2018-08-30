from turtle1 import *
def main():
    nimo1 = Fish("nimo1")
    turtle = Turtle("turrle",30)
    nimo2 = Fish("nimo2")
    nimo3 = Fish("nimo3")
    nimo4 = Fish("nimo4")
    nimo5 = Fish("nimo5")
    print("turtle的初始位置为：{}".format(turtle.start()))
    print("{}的初始位置为：{}".format(nimo2.name,nimo2.start()))
    print("{}的初始位置为：{}".format(nimo3.name,nimo3.start()))
    print("{}的初始位置为：{}".format(nimo4.name,nimo4.start()))
    print("{}的初始位置为：{}".format(nimo5.name,nimo5.start()))
    print("{}的初始位置为：{}".format(nimo1.name,nimo1.start()))
    #print("turtle1:",turtle.location())
    #print("nimo1:",nimo1.location())
    print(turtle.kill(nimo2))
    
if __name__ == "__main__":    
   main()
