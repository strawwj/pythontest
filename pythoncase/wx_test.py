import wx
#对象化开发
app = wx.App()#应用程序对象
frame = wx.Frame(parent = None)#框架窗口对象
frame.Show()#显示框架窗口
app.MainLoop()#进入消息循环
#子类化开发
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None, title = 'My Tools',size = (385,200),pos = (800,300))
        panel = wx.Panel(frame, -1)
        self.button_wjx = wx.Button(panel, -1, '五角星', pos=(50,50),size= (50,25))
        self.Bind(wx.EVT_BUTTON,self.OnButtonWjx,self.button_wjx)
    #event function
        def onButtonWjx(self,event):
            for i in range(5):
                turtle.forward(100)
                turtle.right(144)
        frame.Show()
        return True
app = MyApp()
app.MainLoop()
