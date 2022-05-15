import speech_recognition
import speech_recognition as sr


while True:
    try:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Powiedz cos!")
            audio = recognizer.listen(source)
        print("Powiedziales: ")
        print(recognizer.recognize_google(audio, language="pl-PL"),"\n")

        f = open("kontakty.txt", mode='a', encoding='utf-8')
        f.write(recognizer.recognize_google(audio, language="pl-PL"))
        f.write("\n")
        f.close()


    except:
        continue