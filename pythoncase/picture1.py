#coding:utf-8
def picture():
    import os
    s2 = []
    dic = {}
    l =  os.listdir("/home/pythoncase/picture")
    for i in l:
        s = i.split("_")
        try:
            s1 = s[1]
        except IndexError:
            pass
        s2.append(s1[4:6])
    for i in s2:
        #print(i)
        if i in dic:
            dic[i]+= 1
        else:
            dic[i]= 1
    print(dic)
picture()
