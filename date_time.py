import datetime

import pyttsx3 #pip install pyttsx3

engine = pyttsx3.init()

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def speak_without_print(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = str(datetime.datetime.now().strftime("%H:%M:%S"))
    Time = Time.split(':')
    print("FRIDAY : current time is --> " + str(Time[0]) + ' : ' + str(Time[1]))
    Time = "current time is > " + str(Time[0]) + ' hours and '+ str(Time[1]) +  ' minutes'
    speak_without_print(Time)
#time()

def date():
    Date = datetime.datetime.now().strftime("%d/%m/%Y")
    print("FRIDAY : current date is --> " + Date)
    Date = "current date is >> " + Date
    speak_without_print(Date)
#date()

def greet():
    hour = datetime.datetime.now().hour
    if hour>= 6 and hour<12:
        print('friday : ', end = "")
        speak("good morning")
    elif hour>= 12 and hour<18:
        print('friday : ', end="")
        speak("good afternoon")
    elif hour>= 18 and hour<24:
        print('friday : ', end="")
        speak("good evening")
    else:
        print('friday : ', end="")
        speak("good night")