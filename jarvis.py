import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser 
import os
import smtplib
import time
from PyDictionary import PyDictionary

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18: 
        speak("Good Afternoon!")   
    else:
        speak("Good Evening")    
    speak("I am Jarvis Sir. How may I help you ?")

def takeCommand():
    # It take microphone audio and output string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print (e)
        print ("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('jayeshproject01@gmail.com','<pass>')
    server.sendmail('jayeshproject01@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    wishMe()

    dictionary=PyDictionary()
    #while(1):
    if 1 :
        query = takeCommand().lower()

        #logic for execution based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'meaning of' in query:
            query=query.replace("meaning of","")
            print (dictionary.meaning(query))

        elif 'synonym of' in query:
            query=query.replace("synonym of","")
            print (dictionary.synonym(query))
        
        elif 'antonym of' in query:
            query=query.replace("antonym of","")
            print (dictionary.antonym(query))
        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")   

        elif 'weather' in query:
            webbrowser.open("https://www.bbc.com/weather")

        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0])) 

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'reminder' in query:
             print("What shall I remind you About?")
             text = str(input())
             local_time = input()
             local_time = local_time * 60
             time.sleep(local_time)
             print(text)

        elif 'open code' in query:
            codePath = "C:\\Users\\Jayesh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to jayesh' in query:
            try:
                speak("What should I say ?")
                content = takeCommand()
                to="jayeshkumar306@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Email cant sent at the moment!")
        
        elif 'exit' in query:
            speak("Good Bye !")
            print("Good bye!")
            exit()

        elif 'handsome' in query:
            speak("Vishal Sir is the most handsome person")
            print("Vishal Sir is the most handsome person")

        else:  
            speak("No Instruction has been feed for this Query")
            #for term in query:
            print(query)
            webbrowser.open_new_tab("https://www.google.com.tr/search?q=+" + query) 
