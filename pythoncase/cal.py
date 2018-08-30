a = int(input("please input a num:"))
b = input("please input + - * / :")
c = int(input("please input a num:"))
d = a + c
e = a - c
f = a * c
g = a / c
if (b =='+'):
    print(d)
elif (b== '-'):
    print(e)
elif(b == '*'):
    print(f)
elif(b == '/'):
    print(g)
else:
    print("only :+ - * /")
'''
res = {'+':a+c, '-':a-c, '*':a*c,'/':a/c}
print(res.get(b,"only + - * /:"))
'''
