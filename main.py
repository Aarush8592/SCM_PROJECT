import pyttsx3 #importing modules
import datetime
import speech_recognition as sr
import pyaudio
from pywikihow import search_wikihow
import wikipedia
import webbrowser
from datetime import date
import bs4
from bs4 import BeautifulSoup
import requests
import pywhatkit
import os
import pickle
import random
import random
import keyboard
from keyboard import press_and_release
import googlescrap


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 185)
print(voices[1].id)


def speak(audio):
    print("   ")
    print(f"vipra:{audio}")
    print("   ")
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour and hour <= 12:
        speak("good morning sir")

    elif 12 <= hour and 18 >= hour:
        speak("good after noon sir")
    else:
        speak("good evening sir")
    speak("i am vipra ur coding python assistant")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.7

        audio = r.listen(source,0,5)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}\n")
    except Exception as e:
        # print(e)
        print("say that again please...")
        return ""
    return query

if __name__ == "__main__":
    wish()

    st = datetime.datetime.now().strftime("%d:%M")

    dt = datetime.datetime.now().strftime("%b %d %Y")
    
    speak("how may i help you")
    while True:
        query=takecommand().lower()
        hello=("hello","how are your studies going","are you fine?")
        reply_bye=("goodbye","take care","continue studying","happy studies","good luck for ur exams")
        if("python" in query):
            speak("please enter following details:")
            class pth():
                def intro(self):
                    speak("please enter your name")
                    self.name=input("enter name:")
                    speak("please enter your roll number")
                    self.roll=int(input("enter your roll number:"))
                    speak("enter percentage marks of python in st1:")
                    self.marks=int(input("enter percentage:"))
                    if (self.marks<=40):
                        jasoos='0'
                    elif (self.marks>40 and self.marks<=80):
                        jasoos='1'
                    else:
                        jasoos='-1'
                    
                    speak("topics for st1 were:")
                    speak("1 variable")
                    speak("2 input")
                    speak("3 loops")
                    speak("4 list")
                    if(jasoos=='0'):
                        speak("need improvement")
                        speak("please see this video for variables")
                        vid="https://youtu.be/o-pRdr8IMWg"
                        webbrowser.open(vid)
                        speak("after completing the video please type y")
                        state = "Y"
                        if(state.upper() == "Y"):
                            s = input("enter y if completed watching the video:")
                            speak("thank you for completing the video")
                            speak("please see this video as well for loops")
                            speak("please type y if completed the video:")
                            lo="https://youtu.be/94UHCEmprCY"
                            webbrowser.open(lo)
                            district='Y'
                            if(district.upper()=='Y'):
                                     j=input("please type y if completed the video:")
                                     speak("thank you for completing the video")
                                     speak("please see this last video on list")
                                     lt="https://youtu.be/9OeznAkyQz4"
                                     webbrowser.open(lt)
                                     speak("please type y after completing the video:")
                                     u=input("enter y if completed the video:")
                                     city="Y"
                                     if (city.upper()=='Y'):
                                        speak("please attempt these questions now")
                                        l = "https://search.brave.com/search?q=google&source=desktop"
                                        webbrowser.open(l)
                                                                               
                    elif (jasoos=='1'):
                        speak("you have done very well.")
                        speak("just need a bit of practice")
                        speak("please see this video")
                        vid2="https://www.youtube.com/watch?v=vLqTf2b6GZw"
                        webbrowser.open(vid2)
                        state = "Y"
                        if(state.upper() == "Y"):
                            speak("if complete the video please enter y")
                            s = input("enter y if completed watching the video:")
                            speak("please attempt these questions now.")
                            li="https://search.brave.com/search?q=google&source=desktop"
                            webbrowser.open(li)
                        
                    else:
                        speak("congratulations! you are very hard working")
                        speak("to polish your skills please attempt these questions")
                        hr="https://www.hackerrank.com/domains/python"
                        webbrowser.open(hr)
            s=pth()
            s.intro()
            
        elif("hello" in query):
            reply = random.choice(hello)
            speak(reply)
            
        elif ("go to sleep" in query):
             reply = random.choice(reply_bye)
             speak(reply)
             break
