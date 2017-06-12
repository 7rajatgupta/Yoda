import win32.com.client as win32client
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
