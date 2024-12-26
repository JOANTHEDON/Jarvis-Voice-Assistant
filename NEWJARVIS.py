import operator

import PyQt5
import kit as kit
import pyttsx3
import requests
import speech_recognition as sr
from tkinter import messagebox
import sqlite3
# from siri import Ui_MainWindow
# from StartStop import Ui_MainWindow
import datetime
import os
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit
import smtplib
import sys
import pyjokes
import cv2
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_MainWindow

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)





def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def calculate(statement):
    try:
        result = eval(statement)
        speak(f"The result is {result}")
    except:
        speak("Sorry, I couldn't perform the calculation. Please try again.")





def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")

    else:
        speak("Good Evening Sir")

    speak("Please Tell me How may I help you")

def open_file(filename):
    if "." in filename:
        extension = filename.split(".")[-1]
        if extension in ["txt", "pdf", "doc", "docx", "exe", "html", ""]:
            os.startfile(filename)
        else:
            speak("Sorry, I don't know how to open that file type.")
    else:
        os.startfile(filename)

class MainThread(QThread):
      def __init__(self):
          super(MainThread,self).__init__()
      def run(self):
         self.TaskExecution()

      def take_command(self):
          # it takes microphoen input from user and return string
          r = sr.Recognizer()

          with sr.Microphone() as source:
              print("Listening...")
              r.pause_threshold = 1
              r.adjust_for_ambient_noise(source)
              audio = r.listen(source)
          try:
              print("Recognizing ...")
              query = r.recognize_google(audio, language="en-in")
              print(f"User said:{query} \n")

          except Exception as e:
              # print(e)
              print("Say that again please....")
              speak("I am unable to hear please try again")

              return "None"
          return query

      def TaskExecution(self):
            # speak("This is advance Jarvis")

            wishMe()

            while True:

                self.query = self.take_command().lower()
                if "open notepad" in self.query:
                    speak("Okay opening notepad")
                    npath = "C:\\Windows\\System32\\notepad.exe"
                    os.startfile(npath)
                    speak("Okay i have opened notepad")

                elif "hello" in self.query:
                    speak("Hello sir, how are you ?")
                    if "i am fine" in self.query:
                            speak("that's great, sir")
                    elif "how are you" in self.query:
                            speak("Perfect, sir")
                    elif "thank you" in self.query:
                            speak("you are welcome, sir")


                elif 'close notepad' in self.query:
                    speak("Okay closing notepad")
                    os.system('taskkill /f /im notepad.exe')
                    speak("Okay i have closed notepad")

                elif "open command prompt" in self.query:
                    speak("Okay opening command prompt")
                    os.system('start cmd')
                    speak("Okay i have opened command prompt")

                elif "close command prompt" in self.query:
                    speak("Okay Closing command prompt")
                    os.system('taskkill /f /im cmd.exe')
                    speak("Okay i have opened command prompt")

                elif 'open camera' in self.query:
                    speak("Okay opening Camera")
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, img = cap.read()
                        cv2.imshow('webcame', img)
                        k = cv2.waitKey(50)
                        if k == 27:
                            break;
                    cap.release()
                    cv2.destroyAllWindows()

                elif 'play music' in self.query:
                    try:
                        music_dir = "C:\\Users\\saadn\\Music"
                        songs = os.listdir(music_dir)
                        # rd=random.choice(songs)
                        for song in songs:
                            if song.endswith('.mp3'):
                                os.startfile(os.path.join(music_dir, song))
                            else:
                                speak("No Song Fond")

                    except Exception as e:
                        speak("Unable To Load The Directory")
                        print(e)
                elif 'ip address' in self.query:
                    ip = get('https://api.ipfi.org').text
                    speak(f"your ip address is {ip}")

                elif "wikipedia" in self.query:
                    speak("Searching Wikipedia...")
                    self.query = self.query.replace("wikipidea", "")
                    results = wikipedia.summary(self.query, sentences=2)
                    speak("I Found This On Internet")
                    speak(results)

                elif "open youtube" in self.query:
                    speak("Opening YouTube")
                    webbrowser.open("youtube.com")
                    speak("Ok I Have Open YouTube")

                elif "open google" in self.query:
                    speak("sir , what should i search on google")
                    cm = self.take_command().lower()
                    webbrowser.open(f"{cm}")

                elif "open stackoverflow" in self.query:
                    speak("Ok Sir Opeaning Stack Over Flow Website")
                    webbrowser.open("stackoverflow.com")

                elif "open facebook" in self.query:
                    speak("Opening Facebook")
                    webbrowser.open("facebook.com")
                    speak("Ok I Have Open FaceBook")


                elif "play song on youtube" in self.query:
                    speak("Which Song Would You Like To Play")
                    try:
                        cm = self.take_command().lower()
                        kit.playony(f"{cm}")
                    except Exception as e:
                        speak("Unable To Hear That")

                elif "no thanks" in self.query:
                    speak("Thanks for using me,sir, have a good day")
                    sys.exit()

                elif 'tell me joke' in self.query:
                    speak("I Fond This,")
                    joke = pyjokes.get_joke()
                    speak(joke)

                elif "open website" in self.query:
                    speak("Sure, which website would you like me to open?")
                    website = self.take_command()
                    webbrowser.open_new(f"https://{website}.com")
                    speak("Sir I Do Have Opened The Website")

                elif "open file" in self.query:
                    speak("What is the name of the file?")
                    filename = self.take_command()
                    if filename:
                        open_file(filename)


                # MAIN CODE EXECUTION OF CODE

                elif "batch number" in self.query:
                    speak("Sir Please Wait Fetching The Data")
                    conn = sqlite3.connect("./Database/Information.db")
                    cursor = conn.cursor()
                    batchno = "SELECT Batch_No FROM AccountDB"
                    cursor.execute(batchno)
                    result = cursor.fetchall()
                    speak(f"The Batch Number is {result}")
                    cursor.close()
                    conn.close()

                elif "started by" in self.query:
                    speak("Sir Please Wait Fetching Data")
                    conn = sqlite3.connect("./Database/Information.db")
                    cursor = conn.cursor()
                    startby = "SELECT start_by FROM AccountDB"
                    cursor.execute(startby)
                    result = cursor.fetchall()
                    speak(f"The Batch was Started By{result}")
                    cursor.close()
                    conn.close()

                elif "stop by" in self.query:
                    speak("Sir Please Wait Fetching Data")
                    conn = sqlite3.connect("./Database/Information.db")
                    cursor = conn.cursor()
                    startby = "SELECT stoped_by FROM AccountDB"
                    cursor.execute(startby)
                    result = cursor.fetchall()
                    speak(f"The Batch was Stopped By{result}")
                    cursor.close()
                    conn.close()

                elif "start date" in self.query:
                    speak("Sir Please Wait Fetching Data")
                    conn = sqlite3.connect("./Database/Information.db")
                    cursor = conn.cursor()
                    startby = "SELECT batch_start_date FROM AccountDB"
                    cursor.execute(startby)
                    result = cursor.fetchall()
                    speak(f"Date of Batch Started At{result}")
                    cursor.close()
                    conn.close()

                elif "stop date" in self.query:
                    speak("Sir Please Wait Fetching Data")
                    conn = sqlite3.connect("./Database/Information.db")
                    cursor = conn.cursor()
                    startby = "SELECT batch_end_date FROM AccountDB"
                    cursor.execute(startby)
                    result = cursor.fetchall()
                    speak(f"Date of Batch Ended At{result}")
                    cursor.close()
                    conn.close()

                elif "start time" in self.query:
                    speak("Sir Please Wait Fetching Data")
                    conn = sqlite3.connect("./Database/Information.db")
                    cursor = conn.cursor()
                    startby = "SELECT batch_start_time FROM AccountDB"
                    cursor.execute(startby)
                    result = cursor.fetchall()
                    speak(f"Time of Batch Started At{result}")
                    cursor.close()
                    conn.close()

                elif "end time" in self.query:
                    speak("Sir Please Wait Fetching Data")
                    conn = sqlite3.connect("./Database/Information.db")
                    cursor = conn.cursor()
                    startby = "SELECT batch_end_time FROM AccountDB"
                    cursor.execute(startby)
                    result = cursor.fetchall()
                    speak(f"Time of Batch Ended At{result}")
                    cursor.close()
                    conn.close()

                # END OF BATCHRELATED QUERY

                elif "thank you" in self.query:
                    speak("Thanks for using me,sir, have a good day")
                    sys.exit()


# GUI PART=======================================================================
# ===============================================================================

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)





    def startTask(self):
                 self.ui.movie=QtGui.QMovie("assets\\siri.gif")
                 self.ui.label.setMovie(self.ui.movie)
                 self.ui.movie.start()
                 timer=QTimer(self)
                 timer.timeout.connect(self.showTime)
                 timer.start(1000)
                 startExecution.start()

    def showTime(self):
                current_time =QTime.currentTime()
                current_date = QDate.currentDate()
                label_time=current_time.toString("hh:mm:ss")
                label_date=current_date.toString(Qt.ISODate)
                self.ui.textBrowser.setText(label_date)
                self.ui.textBrowser_2.setText(label_time)




app =  QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())