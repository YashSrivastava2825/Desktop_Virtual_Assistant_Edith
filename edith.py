# pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline,
# and is compatible with both Python 2 and 3.
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')  # for using inbuilt windows voice sapi5
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Edith. Tell how can i help you ")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('yash216800@gmail.com', 'Yash0123')
    server.sendmail('yash216800@gmail.com', to, content)
    server.close()


def takeCommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 0.75
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please,....")
        return "None"
    return query


if __name__ == "__main__":
    speak("Hi Yash")
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing task
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(result)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            webbrowser.open("https://www.youtube.com/watch?v=3jgH5weXYwA")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.2.1\\bin\\pycharm64.exe"
            os.startfile(codePath)

        elif 'email to yash' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "yash216800@gmail.com"
                sendEmail(to, content)
                speak("Email has been send")
            except Exception as e:
                speak("Error! Email was not sent")

        elif 'end' or 'good bye' in query:
            exit()

