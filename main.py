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
    _unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _unverified_https_context

mHeaders = {'''user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6)
           AppleWebKit/537.36 (KHTML, like Gecko)
           Chrome/53.0.2785.143 Safari/537.36'''}
speakNow = win32client.Dispatch("SAPI.SpVoice")
