#coging:utf-8
num = input("请输入一个1～100的整型数：")
try:
    x = int(num)
except:
     pass
if ((1<= x <= 100) and (isinstance(x,int))):
    print("你好棒阿！继续努力")
else:
	print("乖乖，你咋这么不听话呢")

