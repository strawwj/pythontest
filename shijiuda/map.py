import jieba
def Map(files,filename):
    d = {}
    with open(files,'r',encoding='utf8') as f:
        f1 = f.read()
        f2 = jieba.cut(f1)
        for i in f2:
            if i not in ["，","！","、","（","）","\n"]:
                if i in d:
                   d[i]+= 1
                else:
                    d[i]= 1
    with open(filename,"a+",encoding='utf8') as f:
        for k,v in d.items():
            n = k+":"+str(v)
            f.write(n+"\n")
Map("shijiuda.txt1","shijiuda")
Map("shijiuda.txt2","shijiuda")
Map("shijiuda.txt3","shijiuda")
Map("shijiuda.txt4","shijiuda")
   
