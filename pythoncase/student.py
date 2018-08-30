stu =["sdoi",21,'DSF',283]
name = input("please input your name：")
age =int(input("please input your age："))
sex = input("please input your sex：")
code = input("please input your code：")
s= print("学生的姓名：{} 年龄：{} 性别：{} 学号:{}".format(name,age,sex,code))
stu.append(s)
#增
stu.append("stu")
#删
stu.remove('DSF')
#改
stu[1]= 'WJ'
#查
print(stu)
f = open("./stu.txt",'w',encoding = 'utf-8')
stu = str(stu)
f.write(stu)
f.close
