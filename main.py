import win32com.client as win32client
import json
import time
import ssl
import requests
import ctypes
import random
import winshell
import webbrowser
import wikipedia
import wolframalpha
import os
import wx
import speech_recognition as speech
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

# Handle SSL error with requests.packages
#Disable Warnings
requests.packages.urllib.disable_warnings()
# TODO: Get API's
try:
    unverifiedHttpsContext = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = unverifiedHttpsContext

mHeaders = {'''user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)
           AppleWebKit/537.36 (KHTML, like Gecko)
           Chrome/53.0.2785.143 Safari/537.36'''}
speakNow = win32client.Dispatch("SAPI.SpVoice")

videos = ['Videos\\1.mp4', 'Videos\\2.mp4',
          'Videos\\3.mp4', 'Videos\\4.mp4',
          'Videos\\5.mp4', 'Videos\\6.mp4',
          'Videos\\7.mp4']
apiKey = '' #Put your api's key here

#Graphical Interface:
class GUI(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, position = wx.DefaultPosition, size = wx.Size(450, 150), style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN, title = "Yoda")
        panel = wx.Panel(self)
        yodaIcon = wx.Icon('yoda16x16.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(yodaIcon)
        sizer = wx.BoxSizer(wx.VERTICAL)
        windowLabel = wx.StaticText(panel, label = "May the force be with you !!")
        sizer.Add(windowLabel, 0, wx.ALL, 5)
        self.text = wx.TextCtrl(panel, style = wx.TE_PROCESS_ENTER, size = (400, 300))
        self.text.SetFocus()
        self.text.Bind(wx.EVT_TEXT_ENTER, self.onEnter)
        sizer.Add(self.text, 0, wx.ALL, 5)
        panel = SetSizer(sizer)
        self.Show()
        speakNow.speak('''Welcome Back !! Where have you been ?''')

    def onEnter(self, event):
        text = self.text.GetValue()
        text = text.lower()
        link = text.split()
        if text == '':
            r = sr.Recognizer()
            with sr.Microphone() as src:
                audio = r.listen(src)
            try:
                text = r.recognize_google(audio)
                text = text.lower()
                link = text.split()
                self.text.SetValue(text)

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google STT; {0}"
                      .format(e))
            except:
                print("Unknown exception occurred!")
#Action : is to open a webpage.
        if text.startswith('open '):
            try:
                speakNow.Speak("opening "+link[1])
                webbrowser.open('http://www.'+link[1]+'.com')
            except:
                print("The force of Internet isn't with you!")
#Action :  Play Song on Youtube
        elif text.startswith('play '):
            try:
                link = '+'.join(link[1:])
                say = link.replace('+', ' ')
                url = 'https://www.youtube.com/results?search_query='+link
                source_code = requests.get(url, headers=headers, timeout=15)
                plain_text = source_code.text
                soup = BeautifulSoup(plain_text, "html.parser")
                songs = soup.findAll('div', {'class': 'yt-lockup-video'})
                song = songs[0].contents[0].contents[0].contents[0]
                hit = song['href']
                speakNow.Speak("playing "+say)
                webbrowser.open('https://www.youtube.com'+hit)
            except:
                print("The force of Internet isn't with you!")
#Action : Google search :
        elif text.startswith('search '):
            try:
                link = '+'.join(link[1:])
                say = link.replace('+', ' ')
                speakNow.Speak("searching on google for "+say)
                webbrowser.open('https://www.google.co.in/search?q='+link)
            except:
                print("The force of Internet isn't with you!")
#Action : Empty the recycle bin :
        elif text.startswith('empty '):
            try:
                winshell.recycle_bin().empty(confirm=False,
                                             show_progress=False, sound=True)
                print("My force has cleared the remains of the dead !")
            except:
                print("I've been doomed !")
#Action : Open Science related News and headlines.
        elif text.startswith('science '):
            try:
                jsonObj = urlopen('''https://newsapi.org/v1/articles?source=new-scientist&sortBy=top&apiKey=your_API_here''')
                data = json.load(jsonObj)
                i = 1
                speakNow.Speak('''I have something latest and greatest for you from my ancestors on earth !''')
                print(''' ----------SCIENCE NEWS'''+'\n')
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    i += 1
            except:
                print("The force of Internet isn't with you!")
        elif text.startswith('headlines '):

            try:
                jsonObj = urlopen('''https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey=your_API_here''')
                data = json.load(jsonObj)
                i = 1
                speakNow.Speak("Here's something I could find in your country, from my best ally !")
                print('''             ===============TIMES OF INDIA============'''
                +'\n')
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    i += 1
            except Exception as e:
                print(str(e))
#Action : Lock the device:
        elif text.startswith('lock '):
            try:
                speakNow.Speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
            except Exception as e:
                print(str(e))
#Action : user-bored, play videos
        elif text.endswith('bored'):
            try:
                speakNow.Speak("I love Star wars music, but I'll play something to free you from your misery !")
                song = random.choice(videos)
                os.startfile(song)
            except Exception as e:
                print(str(e))
#any-other actions, open a wikipedia page or perform a google search
        else:
            try:

                client = wolframalpha.Client(app_id)
                res = client.query(put)
                ans = next(res.results).text
                print(ans)
                speakNow.Speak(ans)
            except:
                #direct to the wikipedia page
                text = put.split()
                text = ' '.join(put[2:])
                #print(text)
                print(wikipedia.summary(text))
                speakNow.Speak('Searched wikipedia for '+put)
#end onEnter() method.
#Triggering the  GUI
if __name__ == "__main__":
        app = wx.App(True)
        frame = MyFrame()
        app.MainLoop()
#End of main.py
