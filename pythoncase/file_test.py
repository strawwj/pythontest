#coding:utf-8
with open("new.txt","a+") as f:
    f.write("python\n good\n nice\n")
    f.flush()
    f.seek(0,0)
    f.read()
    print(f.read())
