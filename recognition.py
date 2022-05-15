import speech_recognition
import speech_recognition as sr
import tkinter
import sys

#Funkcje
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


#GUI

root = tkinter.Tk()
root.geometry('1024x768')
label = tkinter.Label(root, text='Speech Recognition by Michal')
label.pack()
b = tkinter.Button(root, text='Rozpocznij nagrywanie i zapisz do pliku', command=record)
b.pack()
b_2 = tkinter.Button(root, text='Wyjscie', command=wyjscie)
b_2.pack()
root.mainloop()