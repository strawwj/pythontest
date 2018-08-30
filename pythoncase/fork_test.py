import os
pid = os.fork()
print(pid)
os.chdir('/')#改变环境
os.umask(0)
os.setsid()
pid = os.fork()
print('decond fork !!')
print(pid)
