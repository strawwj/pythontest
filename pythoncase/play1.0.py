#coding:utf-8
import random
rand_num = random.randint(1,100)
count = 0
while True:
    user_num = input('猜猜这个数字的大小：')
    print(rand_num)
    count += 1
    if user_num.isdigit():
        num = int(user_num)
        if num > rand_num:
            print("数字大了")
        elif num < rand_num:
            print("数字小了")
        elif num == rand_num:
            print("恭喜哦！！数字是{},一共猜了多少次{}".format(num,count))
            ask = input("是否继续：y or n").lower().strip()
            if ask == 'y':
                rand_num = random.randint(1,100)
                count = 0
                continue
            else:
                break
    
    else:
        print("请重新输入1～100的整数：")
