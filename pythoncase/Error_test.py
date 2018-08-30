#coding:utf-8
'''
try except
'''
try:
    print(abc)
except NameError as f:
    print("file no define",f)
'''
try except  else
'''
a = 100
try:
    print(a)
except NameError:
    print("file no define")
else:
    print(type(a))
'''
try execpt finally
'''
try:
    open("pig.py")
except FileNotFoundError:
    print("文件不存在")
finally:
    print("your are pig!!!")

