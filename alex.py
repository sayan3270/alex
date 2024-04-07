import random

import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import googlesearch as gs
import random
import pyaudio
import distutils_pytest
import setuptools
import socket
import requests
import wikipedia
import webbrowser
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=3, phrase_time_limit=5)
        r.adjust_for_ambient_noise(source, duration=3)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said:  {query}")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <=12:
        speak("Good morning")
    elif hour >= 12 and hour <=18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I'm Alex . please tell me how can i help you?")

if __name__ == "__main__":
    wish()
    while True:
        query = takeCommand().lower()
        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open adobe reader" in query:
            apath = "C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow("Webcam", img)
                k= cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyWindow()

        elif "play music" in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            for song in songs:
                if song.endswith(".mp3"):
                    os.startfile(os.path.join(music_dir, song))

        #ip adresss not working right now need to debug
        elif "whats my ip address " in query:
            ip = requests.get("https://api.ipify.org").text
            speak("Your IP is:{ip}")

        elif "wikipedia" in query:
            speak("searching Wikipedia....")
            query = query.replace("wikipedia ","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open stack overflow" in query:
            webbrowser.open("www.stackoverflow.com")

        #first page of google is working
        elif "open google" in query:
            speak("Sir, what should I search on Google?")
            query1 = takeCommand().lower()
            first_link = gs.search(query1, num=2, tld="co.in", stop=1, pause=0)
            for i in first_link:
                webbrowser.open_new_tab(i)


        #google search bar is not opening
        elif "open google" in query:
            speak("Sir, what should I search on Google?")
            search_query = takeCommand().lower()
            if 'search' in search_query:
                url = "https://www.google.com.tr/search?q={}".format(search)
                webbrowser.open_new_tab(url)
                search_query = search_query.replace('search', '')
                try:
                    webbrowser.open(f"https://www.google.com/search?q={search_query}")
                except Exception as e:
                    print(f"An error occurred: {e}")

        elif "send message" in query:
            phno = input("Enter the contact number (including country code): ")
            speak("Sir, what message should i type")
            message = takeCommand().lower()
            hr = int(input("Enter the hour (0-23): "))
            min = int(input("Enter the minute (0-59): "))
            pywhatkit.sendwhatmsg(phno, message, hr, min)

        elif "play song on youtube" in query:
            query = takeCommand().lower()
            pywhatkit.playonyt(query)

        elif 'send a mail' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whome should i send")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Sayan.")

        elif 'Why are you here' in query:
            speak("I was created as a Minor project by my Master Sayan ")

        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()




        








