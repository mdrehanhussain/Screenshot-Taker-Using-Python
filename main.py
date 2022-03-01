from tkinter import *
import pyautogui as pad
from datetime import date
import datetime
import time
import pyttsx3
def speak(text):
    robot = pyttsx3.init()
    robot.say(text)
    robot.runAndWait()

gettime = datetime.datetime.now()
getdate = date.today()
year = getdate.strftime("%d-%m-%Y ")
time = time.strftime("%H-%M-%S.PNG")

def screenshot():
    myScreenshot = pad.screenshot()
    myScreenshot.save(r''+ year + time)

screenshot()
speak("Your Screenshot Saved")
