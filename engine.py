import wx
import wikipedia
import pyttsx
import wolframalpha
import os

def speakNow(value):
    engine = pyttsx.init()
    voices = engine.getProperty('voices')
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-30)
    engine.say(value)
    engine.runAndWait()
#--------------End of speakNow--------------

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, pos = wx.DefaultPosition, size = wx.Size(450, 100),style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN, title='YODA')
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        label =  wx.StaticText(panel, label = "I'm Yoda !, At your command my lord.")
        sizer.Add(label, 0, wx.ALL, 5)
        self.text = wx.TextCtrl(panel, style = wx.TE_PROCESS_ENTER, size = (400, 30))
        self.text.SetFocus()
        self.text.Bind(wx.EVT_TEXT_ENTER, self.onEnter)
        sizer.Add(self.text, 0, wx.ALL, 5)
        panel.SetSizer(sizer)
        self.Show()
        speakNow("Yoda, the most wisest living on this planet, Waiting for your command my lord !")
        
