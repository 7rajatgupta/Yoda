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
