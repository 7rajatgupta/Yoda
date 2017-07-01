import wx
import wikipedia
import pyttsx
import wolframalpha
import os

def speakNow(value):
    engine = pyttsx.init()
    #engine = pyttsx.getProperty #Crashes when started first Time

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[4].id)
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
    def onEnter(self, event):
        input = self.text.GetValue()
        # input = input.lower()
        #app_id = '2V3684-LXELTTTJ9J'
        try:
            # wolframalpha
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print(answer)
            speakNow(answer)
        except:
            # wikipedia
            input = input.split(' ')
            input = ' '.join(input[2:])
            print(wikipedia.summary(input))
            speakNow('My ally Wikipedia has suggested that :  '+input)


if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
