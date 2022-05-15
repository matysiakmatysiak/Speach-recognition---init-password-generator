import speech_recognition
import speech_recognition as sr
import tkinter
import sys


def wyjscie():
    sys.exit()

def record():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Powiedz cos!")
        audio = recognizer.listen(source)
    print("Powiedziales: ")
    print(recognizer.recognize_google(audio, language="pl-PL"),"\n")
    f = open('kontakt.txt', mode='a', encoding='utf-8')
    f.write(recognizer.recognize_google(audio, language="pl-PL"))
    f.write("\n")
    f.close()
