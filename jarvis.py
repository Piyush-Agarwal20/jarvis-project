# from pip import main
from datetime import datetime
from xmlrpc.client import Server
import pyttsx3
import speech_recognition as sr
import wikipedia
import wikipediaapi
import webbrowser
import os
import smtplib


engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hr=datetime.now().hour
    if hr>=0 and hr<12:
        speak("good morning!")
    elif hr>=12 and hr<18:
        speak("good afternoon!")
    else:
        speak("good evening!")
    
    speak("i am jarvis sir . how can i help you ")

def takecommand():
    """it takes microphone input from user and return string as output """
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

def sendemail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("piyushagarwal1820@gmail.com","PIYUSH2018")
    server.sendmail("piyushagarwal1820@gmail.com",to,content)
    server.close()

    

if __name__=="__main__":
    wishme()
    while True:
        query=takecommand().lower()

        if "wikipedia" in query:
           speak("searching wikipedia")
           query=query.replace("wikipedia","")
           #results=wikipedia.summary(query,sentences=2)
           b=wikipedia.search(query)
           wiki_wiki = wikipediaapi.Wikipedia('en')
           page_py = wiki_wiki.page(b[0])
           print(page_py.summary[0:200])
           speak(page_py.summary[0:200])
        
        elif "open youtube" in query:
            webbrowser.open("http://www.youtube.com",1)

        elif "youtube search" in query:
            query=query.split(" ")
            query.remove("youtube")
            query.remove("search")
            search=""
            for i in query:
                search = search+i+" "
            a="https://www.youtube.com/results?search_query="
            webbrowser.open(a+search)
        
        elif "open google" in query:
            webbrowser.open("http://www.google.com",1)

        elif "google search " in query:
            query=query.split(" ")
            query.remove("google")
            query.remove("search")
            search=""
            for i in query:
                search = search+i+" "
            a="https://www.google.com/search?q="
            webbrowser.open(a+search)
            
        elif "open amazon" in query:
            webbrowser.open("http://www.amazon.com",1)
        
        elif "open zomato" in query:
            webbrowser.open("http://www.zomato.com",1)

        elif "open tradingview" in query:
            webbrowser.open("https://in.tradingview.com/chart/k8Yatu07/")

        elif "open mail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif "cricket score" in query:
            webbrowser.open("https://www.cricbuzz.com")

        elif "bhai" in query:
            # os.chdir("C://gopal bhai")
            # print(os.getcwd())
            os.startfile("C:\\gopal bhai")

        elif "weather" in query:
            webbrowser.open("https://www.timeanddate.com/weather/india/surat/ext") 

        elif "email to piyush" in query:
            try:
                speak("what should i say?")
                content=takecommand()
                to='piyushagarwal1820@gmail.com'
                sendemail(to,content)
                speak("email has been sent!")
            except Exception as e:
                print(e) 
                speak("sorry! email was not sent")
            

        elif "exit" in query:
            exit()

        elif "open code" in query:
            os.startfile("C:\\Program Files\\Microsoft VS Code\\Code.exe")