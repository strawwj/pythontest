import pickle
d = {'a':10,"b":20}
pickle.dumps(d) #序列化
f = open("f.pickle","wb")
f.flush()
f.close()
pickle.dump(d,f)
