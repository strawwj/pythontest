#coding:utf-8
class MyFile():
    def __init__(self,files,mod):
        self.files = files
        self.mod = mod
    def __enter__(self):
        print("start")
        try:
            self.f = open (self.files,self.mod)
        except FileNotFoundError:
            pass
        return self.f #可以使用open提供的方法  #return self 只可以调用自己定义的方法
    def __exit__(self,e,m,doc):
        print("end")
if __name__ == "__main__":
    with MyFile("stu.txt","a+") as f:#with 为上下文管理器
        print("with end")
        f.seek(0,0)
        f.flush()
        print(f.readlines())
        
