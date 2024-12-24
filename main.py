import PyQt5
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic.properties import QtGui
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from main_fridayui import Ui_MainWindow
import time
import speech_recognition as sr  # pip install SpeechRecognition
import pyttsx3  # pip install pyttsx3 # for speak
import wikipedia  # pip install wikipedia
import webbrowser as wb
import os
import sys
import subprocess  # restart program
import pyautogui  # pip install pyautogui # screenshot
import psutil  # pip install psutil  # cpu and battery performance
from googlesearch import search
import nltk
from nltk.stem import WordNetLemmatizer
import google.generativeai as ai
from nltk.chat.util import Chat, reflections  # pip install nltk
from pair import pairs
import datetime

wnl = WordNetLemmatizer()
chatbot = Chat(pairs, reflections)
API_KEY = "gemini API"  #your API
ai.configure(api_key=API_KEY)
# model = ai.GenerativeModel("gemini-pro")
model = ai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat()


def current_time():
    Time = str(datetime.datetime.now().strftime("%H:%M:%S"))
    Time = Time.split(':')
    Time = "current time is " + str(Time[0]) + ' hours and '+ str(Time[1]) +  ' minutes'
    speak(Time)

def date():
    Date = datetime.datetime.now().strftime("%d/%m/%Y")
    Date = "current date is " + Date
    speak(Date)

def greet():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("good morning")
    elif 12 <= hour < 18:
        speak("good afternoon")
    elif 18 <= hour < 24:
        speak("good evening")
    else:
        speak("good night")

engine = pyttsx3.init()
def speak(audio):
    ui.terminalPrint('friday : '+ audio)
    ui.updateGIF('speaking')
    engine.say(audio)
    engine.runAndWait()
    ui.updateGIF('rest')

def screenshot():
    img = pyautogui.screenshot()
    img.save('RESOURCES\\ss.png')

def cpu():
    usage = str(psutil.cpu_percent())
    cpu_percentage = 'cpu is at ' + usage
    speak(cpu_percentage)
    battery = str(psutil.sensors_battery().percent)
    battery_percentage = 'battery is at ' + battery + ' percent'
    speak(battery_percentage)

def intro():
    ui.terminalPrint('Initializing FRIDAY...\n')
    speak("welcome back sir")
    greet()
    speak("friday at your service, please tell me how can I help you?")

class MainClass(QThread):
    def __init__(self):
        super(MainClass, self).__init__()
        self.query = None

    def run(self):
        self.execute()

    def takeCommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            ui.updateGIF('listening')
            ui.terminalPrint('listening...')
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            ui.terminalPrint("recognizing...")
            ui.updateGIF('loading')
            self.query = r.recognize_google(audio, language='en-in')
        except sr.exceptions.UnknownValueError:
            speak("sorry sir! I could not interpret that! please say that again...")
            self.query = "none"
        except:
            speak("sorry sir! I cannot take commands on voice without a proper internet connection.")
            self.query = "none"
        return self.query

    def execute(self):
        intro()
        a = input("text or voice: ")
        while True:
            if a == 'text':
                self.query = input("you : ")
            else:
                self.query = self.takeCommand().lower()

            list2 = nltk.word_tokenize(self.query)
            self.query = ' '.join([wnl.lemmatize(words) for words in list2])

            if self.query == "friday" or "hello friday" in self.query or "hello" in self.query:
                speak("hello sir, how can I help you")
            elif 'greet' in self.query:
                greet()
            elif 'time' in self.query:
                current_time()
            elif 'date' in self.query:
                date()
            elif 'cpu' in self.query:
                cpu()
            elif 'very good' in self.query or 'well done' in self.query or 'great job' in self.query or 'good job' in self.query:
                speak("all thanks to you sir, it's you who made me capable to do this.")

            elif 'remember that' in self.query:
                speak('what should I remember')
                if a == 'text':
                    data = input()
                else:
                    data = self.takeCommand()
                speak('you told me to remember ' + data)
                remember = open('data.txt', 'w')
                remember.write(data)
                remember.close()

            elif 'what you remember' in self.query:
                remember = open('data.txt', 'r')
                speak('you told me to remember that ' + remember.read())

            elif ('search' in self.query or 'open' in self.query) and (
                    'in' in self.query or 'on' in self.query) and 'google' in self.query:
                ui.updateGIF('loading')
                ui.terminalPrint("searching...")
                engine.say('searching')
                engine.runAndWait()
                #speak('searching')
                self.query = self.query.replace("google", "")
                self.query = self.query.replace("search", "")
                self.query = self.query.replace("in", "")
                self.query = self.query.replace("on", "")
                self.query = self.query.replace("open", "")

                try:
                    result = self.query
                    self.query = [i for i in search(self.query, tld="co.in", num=1, stop=1, pause=2)]
                    wb.open_new_tab(self.query[0])
                    result = str("opening" + result + "on your screen...")
                    speak(result)
                except Exception as e:
                    speak('sorry sir! cannot access google without a proper internet connection.')
                ui.updateGIF('rest')

            elif 'wiki' in self.query or 'wikipedia' in self.query:
                ui.updateGIF('loading')
                ui.terminalPrint("searching...")
                engine.say('searching')
                engine.runAndWait()
                self.query = self.query.replace("wikipedia", "")
                self.query = self.query.replace("wiki", "")

                try:
                    speak(wikipedia.summary(self.query, sentences=1))
                except wikipedia.requests.exceptions.ConnectionError as e:
                    print(e)
                    speak('sorry sir! cannot access wikipedia without a proper internet connection.')
                except wikipedia.exceptions.DisambiguationError as e:
                    print(e)
                    speak('multiple results found! please try again with more specific query')
                except Exception as e:
                    print(e)
                    speak("no result found in wikipedia.")

            elif 'screenshot' in self.query:
                screenshot()
                speak('screenshot taken')

            elif 'play songs' in self.query or 'play song' in self.query:
                songs_dir = r"C:\music"
                songs = os.listdir(songs_dir)
                print(os.startfile(os.path.join(songs_dir, songs[0])))

            elif 'logout system' in self.query:
                speak('logging out system')
                ui.updateGIF('loading')
                os.system("shutdown -l")
            elif 'shutdown system' in self.query or (
                    ('shutdown' in self.query or 'switch off' in self.query) and 'system' in self.query):
                ui.updateGIF('loading')
                speak("shutdown system")
                os.system("shutdown /s /t 1")
            elif 'reboot system' in self.query or (
                    ('reboot' in self.query or 'restart' in self.query) and 'system' in self.query):
                ui.updateGIF('loading')
                speak("rebooting system")
                os.system("shutdown /r /t 1")

            elif ('reboot' in self.query or 'restart' in self.query) and (
                    'yourself' in self.query or 'friday' in self.query):
                ui.updateGIF('loading')
                speak('okay sir, rebooting.')
                ui.terminalPrint('rebooting...')
                subprocess.run([sys.executable] + sys.argv)

            elif 'switch to text' in self.query:
                a = 'text'
                speak('commands are switched to text successfully.')
            elif 'switch to voice' in self.query:
                a = 'voice'
                speak('commands are switched to voice successfully.')

            elif 'stop listening' in self.query or 'pause' in self.query or 'mute' in self.query:
                speak("stopped listening...! enter any key to resume.")
                input()
                speak("started listening...")

            elif 'go offline' in self.query or 'go off' in self.query:
                speak("ok sir, going down, have a nice day")
                greet()
                ui.updateGIF('loading')
                ui.close()

            elif self.query == 'none':
                pass
            else:
                response = chatbot.respond(self.query)  # pair response
                if response == "":
                    ui.updateGIF('loading')
                    # response = chat.send_message(self.query).text # gemini response
                    # response = response.replace("*", "")
                    # response = response.split(".")
                    response = ["no data for this in database, please update the database."]
                    print(response[0])
                    speak(response[0])
                else:
                    speak(response)

startExecution = MainClass()

class  ui_friday(QMainWindow):
    def __init__(self):
        super(ui_friday, self).__init__()
        self.oldPosition = PyQt5.QtCore.QPoint()
        self.fridayui = Ui_MainWindow()
        self.fridayui.setupUi(self)

        self.fridayui.logo_button.clicked.connect(lambda: self.minimizeWin('full'))
        self.fridayui.close_button.clicked.connect(self.close)
        self.fridayui.min_button.clicked.connect(lambda: self.minimizeWin('min'))

        self.fridayui.show_search_bar.clicked.connect(self.toggleSearch)

        self.fridayui.send_button.clicked.connect(self.manualCodeFromTerminal)

        self.showterminal = False
        self.status_icon = False
        self.showSearch = False
        self.fridayui.send_button.raise_()

        self.fridayui.show_icon.stateChanged.connect(self.statusCB)
        self.fridayui.show_terminal.stateChanged.connect(self.terminalCB)

        self.runAllGIF()

        startExecution.start()

    def minimizeWin(self, type):
        if type == 'full':
            if self.showterminal == True:
                self.resize(600, 549)
            else:
                self.resize(600, 200)
        elif type == 'min':
            if self.status_icon == True:
                self.resize(600, 200)
            else:
                self.resize(200, 200)


    def ToggleMuteBTN(self, checked):
        if checked:
            MainClass.ToggleMute(self, True)
        else:
            MainClass.ToggleMute(self, False)

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self, event):
        d = PyQt5.QtCore.QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + d.x(), self.y() + d.y())
        self.oldPosition = event.globalPos()

    def toggleSearch(self, checked):
        if checked:
            self.showSearch = True
            self.fridayui.input_frame.show()
            self.fridayui.input_frame1.hide()

        else:
            self.showSearch = False
            self.fridayui.input_frame.hide()
            self.fridayui.input_frame1.show()

    def runAllGIF(self):

        self.fridayui.movie = QtGui.QMovie("RESOURCES/TERMINAL_FRAME.gif")
        self.fridayui.label.setMovie(self.fridayui.movie)
        self.fridayui.movie.start()

        self.fridayui.movie = QtGui.QMovie("RESOURCES/logo1.gif")
        self.fridayui.logo_label.setMovie(self.fridayui.movie)
        self.fridayui.movie.start()

        self.fridayui.movie = QtGui.QMovie("RESOURCES/listening.gif")
        self.fridayui.listening.setMovie(self.fridayui.movie)
        self.fridayui.movie.start()

        self.fridayui.movie = QtGui.QMovie("RESOURCES/loading.gif")
        self.fridayui.loading.setMovie(self.fridayui.movie)
        self.fridayui.movie.start()

        self.fridayui.movie = QtGui.QMovie("RESOURCES/speaking.gif")
        self.fridayui.speaking.setMovie(self.fridayui.movie)
        self.fridayui.movie.start()

        #startExecution.start()

    def updateGIF(self, state):
        if state == "speaking":
            self.fridayui.speaking.raise_()
            self.fridayui.speaking.show()
            self.fridayui.listening.hide()
            self.fridayui.logo_label.hide()
            self.fridayui.loading.hide()
        elif state == "listening":
            self.fridayui.listening.raise_()
            self.fridayui.listening.show()
            self.fridayui.logo_label.hide()
            self.fridayui.speaking.hide()
            self.fridayui.loading.hide()
        elif state == "loading":
            self.fridayui.loading.raise_()
            self.fridayui.loading.show()
            self.fridayui.logo_label.hide()
            self.fridayui.speaking.hide()
            self.fridayui.listening.hide()
        else:
            self.fridayui.logo_label.raise_()
            self.fridayui.logo_label.show()
            self.fridayui.speaking.hide()
            self.fridayui.listening.hide()
            self.fridayui.loading.hide()
        self.fridayui.logo_button.raise_()

        #startExecution.start()

    def terminalPrint(self, text):
        self.fridayui.terminal_box.appendPlainText(text)

    def manualCodeFromTerminal(self):  #pending
        if self.fridayui.input_box.text():
            cmd = self.fridayui.input_box.text()
            self.fridayui.input_box.clear()
            self.fridayui.terminal_box.appendPlainText(f"you: {cmd}")

            if cmd == 'exit' or 'bye' in cmd:
                ui.close()
            else:
                pass

    def terminalCB(self, checked):
        if checked:
            self.showterminal = True
            self.resize(600, 549)
        else:
            self.showterminal = False
            self.resize(600, 200)

    def statusCB(self, checked):
        if not checked:
            self.status_icon = True
            self.resize(200, 200)
        else:
            self.status_icon = False


app = QApplication(sys.argv)
ui = ui_friday()
ui.show()
sys.exit(app.exec_())
