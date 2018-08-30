#coding:utf-8
import csv
class Message():
    def insert(self,name,tele):
        self.name = name
        self.tele = tele
        with open("stu.csv","wb") as f:
            writer = csv.writer(f)
            writer.writerow(["name","tele"])
            data =[("{}".format(self.name),"{}".format(self.tele))]
            data1 = writer.writerows(data)
        return data1
    def del1(self,n):
        with open("stu.csv","r") as f:
            d = f.readlines()
            d[n] = ''
        with open("stu.csv","wb") as f:
            f.writelines(d)
    def show(self):
        with open("stu.csv","r") as f:
             a = f.readlines()
        return a
    def change(self,name,other):
        with open("stu.csv","r") as f:
             a1 = csv.reader(f)
             for i in a1:
                if i[0] ==  name:
                    i[0] = other
        with open("stu.csv","ab") as f:
             writer = csv.writer(f)
    def main(self):
        num = input("1 | 2 | 3 | 4 :")
        if num == 1:
            return self.show()
        elif num == 2:
            n = input("n:")
            self.del1(n)
        elif num == 3:
            name = input("name:")
            tele = input("tele:")
            self.insert(name,tele)
        elif num == 4:
            name = input("name:")
            other = input("other:")
            self.change(name,other)
        else:
            print("please input 1 or 2 or 3 or 4")
if __name__ == "__main__":
    #m = Message()
    #m.insert("eirweuf","93432")
    #m.del1(1)
    #print(m.show())
    m1 = Message()
    #m1.insert("sa","392")
    #print(m1.show())
    #m1.change("sa","as")
    print(m1.main())
