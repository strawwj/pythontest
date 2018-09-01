def end(dFile,sFolder):
    d = {}
    '''
    for root,dirs,files in os.walk(sFolder):
        for f in files:
            if f.endswith("")
    '''
    with open(dFile,'r',encoding='utf8') as f:
        for line in f:
            k,v = line.split(":")   
            if k in d:
                d[k]= int(d[k])+ int(v)
            else:
                d[k]= v  

    l = []
    for k,v in d.items():
        l.append(k + ' '+ ' '+ str(v)+'\n')
    with open("gshijiuda.txt",'w',encoding='utf8') as f:
         f.writelines(l)
            
end("shijiuda","")             
