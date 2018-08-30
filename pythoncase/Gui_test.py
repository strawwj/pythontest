import tkinter
import turtle
root = tkinter.Tk()
label = tkinter.Label(root,text = "你好")
label.pack()
button1 = tkinter.Button(root,text="五角星")
button1.pack()

#menu
menu_file = tkinter.Menu(root)
file_submenu = tkinter.Menu(menu_file,tearoff = 0)
file_submenu.add_command(label = "打开")
file_submenu.add_command(label = "保存")
menu_file.add_cascade(label = "文件",menu = file_submenu)
root.config(menu = menu_file)
#event function
def wjx(event):
    for i in range(5):
        turtle.forward(200)
        turtle.right(144)
#bind
button1.bind('<Button-1>', wjx)
root.mainloop()
