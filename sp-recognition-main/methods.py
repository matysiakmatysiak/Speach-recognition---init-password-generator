import speech_recognition
import speech_recognition as sr
import tkinter
import sys
from note import Password
from air import air_condition

def wyjscie():
    sys.exit()

def record():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mów")
        audio = recognizer.listen(source)
    print("Powiedziałeś: ")
    print(recognizer.recognize_google(audio, language="pl-PL"),"\n")
    if recognizer.recognize_google(audio, language="pl-PL") == 'Stwórz mi hasło':
        Password()
    elif recognizer.recognize_google(audio, language="pl-PL") == 'podaj mi stan powietrza':
        air_condition()
    else:
        print('zjebałeś')
