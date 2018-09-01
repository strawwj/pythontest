def show(filename):
    dictList = []
    flag = True
    with open(filename,'r',encoding='utf8') as f:
        print('%-10s%10s'%('word','count'))
        print('-'*25)
        while flag:
            f1 = f.readline()
            #print(f1) 
            f2 = f1.split()
            if f1 != "" and f2 != [] and int(f2[1])>100:
                print('%-12s    %6s'%(f2[0],f2[1]))
            if f1 == "":
                break
show("gshijiuda.txt")
