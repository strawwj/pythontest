import os 
import os.path
def dataSplit(sFile,dFolder):
    flag = True
    n = 0
    if not os.path.isdir(dFolder):
        os.mkdir(dFolder)
    with open(sFile,'r',encoding = 'utf8') as f:
        while flag:
            n += 1 
            filename = os.path.join(dFolder,os.path.split(sFile)[1]+str(n))
            with open(filename,"a+",encoding='utf8') as f2:
                for i in range(100):
                    f1 = f.readline()
                    if f1!= "":
                        f2.write(f1)
                    else:
                        flag = False
                        break
                     
dataSplit("shijiuda.txt","shijiuda")
