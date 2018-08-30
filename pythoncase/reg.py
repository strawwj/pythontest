from win32gui import CreateRoundRectRgn, GetWindowRect
from winxpgui import SetWindowRgn
import wx
from configer import Cfg
from hooks.skinhook import SkinButton, SkinMinSizeButton, SkinCloseButton, SkinInput, InstallSkin
from tools.common import  MessageBox
import wx.lib.hyperlink as hyperlink
from ui.dialogs.setttingdlg import SettingDlg
from uilogic.frameinf import ILoginUIHandler
from ui.image import ImageCenter

UIHandler=ILoginUIHandler
class LoginFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, -1, 'E时代安全电子文档V2.0',wx.DefaultPosition, (380, 280),style=wx.NO_BORDER|wx.FRAME_SHAPED)
		self.panel=LoginPanel(self,(380,280))
		self.SetDefaultItem(self.panel.btnLogin)

		self.panel.Bind(wx.EVT_MOTION,self.OnMouseMove)
		self.panel.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
		self.panel.Bind(wx.EVT_LEFT_UP,self.OnMouseUp)

		self.delta = (0,0)
		self.SetBalloonShape()
		self.Center()

	def OnMouseDown(self,event):
		self.panel.CaptureMouse()
		x, y =  self.ClientToScreen(event.GetPosition())
		originx, originy = self.GetPosition()
		dx = x - originx
		dy = y - originy
		self.delta = ((dx, dy))

	def OnMouseUp(self, evt):
		if self.panel.HasCapture():self.panel.ReleaseMouse()

	def OnMouseMove(self, evt):
		if evt.Dragging() and evt.LeftIsDown():
			x, y = self.ClientToScreen(evt.GetPosition())
			fp = (x - self.delta[0], y - self.delta[1])
			self.Move(fp)


	def SetBalloonShape(self):
		left,top,right,bottom=GetWindowRect(self.GetHandle())
		hrgn=CreateRoundRectRgn(left,top,right,bottom,5,5)
		SetWindowRgn(self.GetHandle(),hrgn,True)

#		width, height = self.GetSize()
#		bmp = wx.EmptyBitmap(width,height)
#		dc = wx.BufferedDC(None, bmp)
#		dc.DrawRoundedRectangle(0, 0, width-1, height-1,3)
#		dc.EndDrawing()
#		self.hasShape = self.SetShape(wx.RegionFromBitmapColour(bmp, wx.Colour(0,0,0)))

	def SaveName(self):
		Cfg.c_lastname=self.panel.username \
		if Cfg.bool(Cfg.c_savename) else ''

	def ClearPasswrod(self):
		self.panel.pwdText.SetValue('')


class LoginPanel(wx.Panel):

	def __init__(self,parent,size):
		wx.Panel.__init__(self,parent,-1,size=size)

		self.bgBmp =ImageCenter.WLoginBgBmp.GetBitmap()
		self.logoBmp=ImageCenter.WLogoBmp.GetBitmap()

#		self.btnLogin=wx.Button(self, -1, '登录')
#		self.btnSetting=wx.Button(self,-1,  '设置')

		self.btnLogin=SkinButton(self, -1, '登录')
		self.btnLogin.SetDefault()
		self.btnSetting=SkinButton(self,-1,  '设置')

		self.minBth=SkinMinSizeButton(self)
		self.closeBth=SkinCloseButton(self)

		self.minBth.BindMinSize(parent)
		self.closeBth.BindClose(parent)

		self.nameText=SkinInput(self,size=(190,30),fontsize=11,nullText='帐号')
		self.pwdText=SkinInput(self,size=(190,30),style=wx.TE_PASSWORD,fontsize=11,nullText='密码')
		#self.txtUserName,self.txtPwd=self.namePanel.GetTextCtrl(),self.pwdPanel.GetTextCtrl()

		self.nameText.SetValue(Cfg.c_lastname if Cfg.c_savename else '')

		self.pwdText.SetValue('')

		self.reglink=hyperlink.HyperLinkCtrl(self, -1,u"注册账号")
		self.reglink.SetBackgroundColour('#f9f1f7')
		#self.forgetPwdlink=hyperlink.HyperLinkCtrl(panel, -1, "忘记密码")
		self.reglink.UnsetToolTip()
		self.reglink.Bind(hyperlink.EVT_HYPERLINK_LEFT,self.EvtReglinkClick)
		self.reglink.AutoBrowse(False)
		self.reglink.EnableRollover(True)
		self.reglink.SetUnderlines(False,False,True)
		self.reglink.OpenInSameWindow(True)
		self.reglink.UpdateLink()


		self.rebName = wx.CheckBox(self, -1, "记住帐号")
		self.rebName.SetValue(Cfg.bool(Cfg.c_savename))

		self.username=self.nameText.GetValue()

		self.Bind(wx.EVT_PAINT,self.OnPaint)
		self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
		self.Bind(wx.EVT_BUTTON, self.BthLoginClick, self.btnLogin)
		self.Bind(wx.EVT_BUTTON, self.BthSettingClick, self.btnSetting)




	def OnPaint(self,evt):
		dc = wx.BufferedPaintDC(self)
		if not dc:
			dc = wx.ClientDC(self)
			rect = self.GetUpdateRegion().GetBox()
			dc.SetClippingRect(rect)
		dc.Clear()
		dc.DrawBitmap(self.bgBmp, 0, 0)
		rect=self.GetClientRect()
		y=145
		x=100
		dc.DrawBitmap(self.logoBmp,10,y-8)
		self.nameText.SetDimensions(x,y,self.nameText.width,self.nameText.height)
		w,h=self.reglink.GetClientSize()
		self.reglink.SetDimensions(x+self.nameText.width+10,y+8,w,h)
		y+=35
		self.pwdText.SetDimensions(x,y,self.pwdText.width,self.pwdText.height)

		y+=self.pwdText.height+10
		w,h=self.rebName.GetSizeTuple()

		self.rebName.SetDimensions(x,y,w,18)

		x=rect.x +rect.width-self.closeBth.width-1
		self.closeBth.SetDimensions(x,1,
			self.closeBth.width, self.closeBth.height-1)
		x-=self.minBth.width
		self.minBth.SetDimensions(x, 1,
			self.minBth.width, self.minBth.height-1)

		x=rect.x + 10
		y=rect.y +rect.height-32
		self.btnSetting.SetDimensions(x,y,self.btnSetting.width, self.btnSetting.height)

		#w,h=self.btnLogin.GetClientSizeTuple()

#		x=rect.x+rect.width - w-10
#		self.btnLogin.SetDimensions(x,y,w,h)

		x=rect.x+rect.width - self.btnLogin.width-10
		self.btnLogin.SetDimensions(x,y,self.btnLogin.width, self.btnLogin.height)





	def BindEvent(self):
		self.Bind(wx.EVT_BUTTON, self.BthLoginClick, self.btnLogin)
		self.Bind(wx.EVT_BUTTON, self.BthSettingClick, self.btnSetting)



	def BthLoginClick(self, event):
		name, pwd = self.nameText.GetValue().strip(), self.pwdText.GetValue().strip()

		Cfg.c_savename=str(self.rebName.IsChecked())
		self.username=self.nameText.GetValue()

		if name == "":
			MessageBox( '请输入用户名！')
		elif pwd == "":
			MessageBox('请输入密码！')
			self.nameText.SetFocus()

		else:
			UIHandler.OnLogin(self,name,pwd)


	def EvtReglinkClick(self,evt):
		UIHandler.OnRegister()


	def BthSettingClick(self, evt):
		dlg = SettingDlg(self)
		dlg.ShowModal()
		dlg.Destroy()
##############################################
class AbstractButton(wx.Window):

	def __init__(self,parent,id=-1,label=wx.EmptyString,pos=wx.DefaultPosition,
	             size=wx.DefaultSize, style=0,
	             validator=wx.DefaultValidator,name=wx.ButtonNameStr):

		wx.Window.__init__(self,  parent, id,pos,size,style,name)
		self._label=label
		self.width,self.height=self.ComputerBestSize()
		self.SetSize(wx.Size(self.width,self.height))
		self.SetTransparent(0)
		self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
		self._onFouce=self._keyDown=self._mouseIn=self._mouseDown=False
		self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)
		self.Bind(wx.EVT_LEFT_UP,self.OnMouseUp)

		self.Bind(wx.EVT_LEAVE_WINDOW,self.OnMouseLeave)
		self.Bind(wx.EVT_ENTER_WINDOW,self.OnMouseEnter)
		self.Bind(wx.EVT_ERASE_BACKGROUND,lambda evt:evt.Skip())
		self.Bind(wx.EVT_PAINT,self.OnPaint)
		self.Bind(wx.EVT_SET_FOCUS,self.OnFouce)
		self.Bind(wx.EVT_KILL_FOCUS,self.OnLoseFocue)

		self.Bind(wx.EVT_BUTTON,self.OnPress)

		self.mouseInBmp=None
		self.mouseDownBmp=None
		self.mouseOutBmp=None
		self.onFouceBmp=None

	def SetDefault(self):
		def OnKey(evt):
			if evt.GetKeyCode() in (wx.WXK_RETURN,wx.WXK_NUMPAD_ENTER):
				self.SendButtonCmd()
			else:
				evt.Skip()
		self.GetParent().Bind(wx.EVT_CHAR_HOOK,OnKey)


	def SetLabel(self,label):
		self._label=label

	def GetLabel(self):
		return self._label

	def OnPress(self,event):
		self._keyDown=True
		self.Refresh()
		self._keyDown=False
		event.Skip()

	def OnFouce(self,event):
		self._onFouce=True
		self.Refresh()
		event.Skip()

	def OnLoseFocue(self,event):
		self._onFouce=False
		self.Refresh()
		event.Skip()


	def ComputerBestSize(self):
		label=self.GetLabel()
		#return default
		if not label:return 24,21
		#computer best size
		fontLen=len(label)
		width,height=65,26
		if fontLen>2:width+=5*(fontLen-2)
		return width,height


	def OnMouseEnter(self,event):
		self._mouseIn = True
		self.Refresh()
		event.Skip()

	def OnMouseLeave(self,event):
		self._mouseIn = False
		self.Refresh()
		event.Skip()

	def OnMouseDown(self,event):
		self._mouseDown = True
		self.Refresh()
		event.Skip()

	def OnMouseUp(self,event):
		self._mouseDown = False
		self.Refresh()
		event.Skip()
		self.SendButtonCmd()

	def DrawButtion(self,dc):
		if self._mouseDown or self._keyDown:
			dc.DrawBitmap(self.mouseDownBmp,0,0)
		elif self._mouseIn:
			dc.DrawBitmap(self.mouseInBmp,0,0)
		elif self._onFouce:
			dc.DrawBitmap(self.onFouceBmp,0,0)
		else:
			dc.DrawBitmap(self.mouseOutBmp,0,0)



	def OnKeyDown(self,event):
		self._keyDown=True
		self.Refresh()
		event.Skip()

	def OnKeyUp(self,event):
		if self._keyDown:
			self._keyDown=False
			self.Refresh()
			event.Skip()
			self.SendButtonCmd()
		else:
			event.Skip()


	def DrawCenterText(self,dc):
		labelText=self.GetLabel()
		if not labelText:return
		w,h=self.GetTextExtent(labelText)
		w2,h2=self.GetClientSizeTuple()
		x,y=(w2-w)/2,(h2-h)/2
		dc.DrawText(labelText,x,y)

	def SendButtonCmd(self):
		event = wx.CommandEvent(wx.wxEVT_COMMAND_BUTTON_CLICKED, self.GetId())
		event.SetInt(0)
		event.SetEventObject(self)
		self.GetEventHandler().ProcessEvent(event)
		event.Skip()

class SkinCloseButton(AbstractButton):

	def __init__(self,parent):
		AbstractButton.__init__(self,parent,style=wx.NO_BORDER)
		self.mouseInBmp=ImageCenter.WCloseInBmp.GetBitmap()
		self.mouseDownBmp=ImageCenter.WCloesOutBmp.GetBitmap()
		self.onFouceBmp=self.mouseOutBmp=ImageCenter.WCloesOutBmp.GetBitmap()


	def BindClose(self,frame):
		frame.Bind(wx.EVT_BUTTON,
			lambda evt:win32gui.SendMessage(frame.GetHandle(),
				win32con.WM_CLOSE,0,0),self)



	def OnPaint(self, event):
		dc = wx.BufferedPaintDC(self)
		self.DrawButtion(dc)
#####################################################
class SkinMaxSizeButton(AbstractButton):
	def __init__(self,parent):
		AbstractButton.__init__(self,parent,style=wx.NO_BORDER)
		self.mouseInBmp=ImageCenter.WMaxInBmp.GetBitmap()
		self.mouseDownBmp=ImageCenter.WMaxOutBmp.GetBitmap()
		self.onFouceBmp=self.mouseOutBmp=ImageCenter.WMaxDownBmp.GetBitmap()


	def BindMaxSize(self,frame):
		frame.Bind(wx.EVT_BUTTON,
			lambda evt:win32gui.SendMessage(frame.GetHandle(),
				win32con.WM_SYSCOMMAND,
				win32con.SC_MAXIMIZE,0),self)




	def OnPaint(self, event):
		dc = wx.BufferedPaintDC(self)
		self.DrawButtion(dc)
#####################################################
class SkinMinSizeButton(AbstractButton):
	def __init__(self,parent):
		AbstractButton.__init__(self,parent,style=wx.NO_BORDER)
		self.mouseInBmp=ImageCenter.WMinInBmp.GetBitmap()
		self.mouseDownBmp=ImageCenter.WMinOutBmp.GetBitmap()
		self.onFouceBmp=self.mouseOutBmp=ImageCenter.WMinDownBmp.GetBitmap()


	def BindMinSize(self,frame):
		frame.Bind(wx.EVT_BUTTON,
			lambda evt:
			win32gui.SendMessage(frame.GetHandle(),
				win32con.WM_SYSCOMMAND,
				win32con.SC_MINIMIZE,0),self)



	def OnPaint(self, event):
		dc = wx.BufferedPaintDC(self)
		self.DrawButtion(dc)




if __name__=='__main__':

	app=wx.PySimpleApp()
	f=LoginFrame()
	f.Show()
	app.MainLoop()
