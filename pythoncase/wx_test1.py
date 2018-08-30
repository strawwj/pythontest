import wx
#对象化开发
app = wx.App()#应用程序对象
frame = wx.Frame(parent = None)#框架窗口对象
frame.Show()#显示框架窗口
app.MainLoop()#进入消息循环
#子类化开发
class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent = None, title = 'My Chat',size = (520,450))
        panel = wx.Panel(frame, -1)
        label_All = wx.StaticText(panel, -1,"聊天记录")#-1默认布局
        self.textAll = wx.TextCtrl(panel,-1,style = wx.TE_MULTLINE)
        label_Say = wx.StaticText(panel, -1,"我要说的话")#-1默认布局
        self.textSay = wx.TextCtrl(panel,-1,style = wx.TE_MULTLINE)
        self.sent_button = wx.Button(panel, -1, '发送')
        self.clear_button= wx.Button(panel, -1, '清空')
        self.Bind(wx.EVT_BUTTON,self.onSentButton,self.sent_button)#按钮事件
        self.Bind(wx.EVT_BUTTON,self.onClearButton,self.clear_button)
        #boxSizer
        btnSizer = wx.BoxSizer()
        btnSizer.Add(self.btn_clear,propertion=0)
        btnSizer.Add(self.btn_sent,propertion = 0)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(label_All,propertion= 1,flag= wx.ALIGN_CENTER_VERTICAL)
        mainSizer.Add(self.textAll,propertion= 0,flag=wx.EXPAND)
        mainSizer.Add(label_Say,propertion= 0,flag=wx.ALIGN_CENTER_VERTICAL)
        mainSizer.Add(self.textSay,propertion= 0,flag=wx.EXPAND)
        mainSizer.Add(btnSizer,propertion= 0)
        panel.SetSizer(mainSizer)
        frame.Show()
        return True
    #event function
    def onSentButton(self,event):
        userinput = self.textSay.GetValue()
        self.textSay.Clear()
        inmsg = 'You say: {}\n'.format(userinput)
        self.testAll.AppendText(inmsg)#appendtext向尾部添加文本
    def onClearButton(self, event):
        self.textAll.Clear()
app = MyApp()
app.MainLoop()
