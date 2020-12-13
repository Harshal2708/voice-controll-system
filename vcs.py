import pyttsx3
# Project description pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries it works offline
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from instabot import Bot
import requests
from bs4 import BeautifulSoup


engine = pyttsx3.init('sapi5')
# for microsoft..sapi5(search google)
voices = engine.getProperty('voices')

#print(voices[0].id)

engine.setProperty('voice',voices[0].id)
# TTS_MS_EN-US_ZIRA_11.0(voice)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if  hour==0 and hour<12:
        speak ('good morning')
    elif hour==12 and hour<18:
        speak("good afternoon")
    elif hour>18:
        speak('good evening')

    speak("i am Computer please tell me ,how may i help you")

def takeCommand():
    # it takes microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listning...')
       # r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        c = r.recognize_google(audio)
        print(f"user said: {c}\n")
    except Exception as e:
      #  print(e)   just to see error
        print("sorry ,try it again...")
        return "None"
    return c
if __name__ == '__main__':
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
        #logic for executing task
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=2) #to return to sentences
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            chrome_path = 'C:\\Users\\Harshal\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

            speak("what to search in youtube.")
            ysearch=takeCommand().lower()
            webbrowser.get("chrome").open_new("http://www.youtube.com/results?search_query =".join(ysearch))

        elif 'open google' in query:
            g = 'https://www.google.com/search?q='
            chrome_path = 'C:\\Users\\Harshal\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe'
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser(chrome_path))
            speak("what to search in google.")
            gsearch = takeCommand().lower()
            webbrowser.get("chrome").open_new(g+gsearch)

        elif 'play music' in query:
            music_dir= 'C:\\Users\\Harshal\\Desktop\\music'
            songs= os.listdir(music_dir)  #list songs of folder
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0])) #for first song in library
        elif 'time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            print(strTime)
        elif 'calculator' in query:
            codepath= "C:\\Windows\\System32\\calc.exe"
            os.startfile(codepath)
        elif 'send email' in query:
            try:
                speak("what should i say..?")
                content=takeCommand()
                to = 'adpawar1999@gmail.com'
                #sendEmail(to,content)
            except Exception as e:
                print(e)
                speak("sorry unable to send mail")
        elif 'instagram' in query:
            URL = "https://www.instagram.com/{}/"
            def scrape(username):
                full_url = URL.format(username)
                r = requests.get(full_url)
                s = BeautifulSoup(r.text, "lxml")

                tag = s.find("meta", attrs={"name": "description"})
                text = tag.attrs['content']
                main_text = text.split("-")[0]
                return main_text

            USERNAME = "call_me_shrey36"
            data = scrape(USERNAME)
            print(data)
            speak(data)

        elif 'photo' in query:
            try:
                bot = Bot()

                bot.login(username="Username",
                          password="********")

                bot.upload_photo(r"C:\Users\Harshal\Desktop\Banner.png",
                                 caption="Technical Scripter Event 2019")
            except Exception as e:
                print(e)
                speak("sorry unable to post photo")

        elif 'create file' in query:
            try:
                f = open(r"C:\Users\Harshal\Desktop\hello.txt", mode='w')
                speak('Enter no of lines to be entered')
                n= int(takeCommand().lower())
                for i in range(1,n+1):
                    speak(f'line {i} is')
                    filewrite = takeCommand().lower()
                    f.write(f'\n{filewrite}')
                f.close()
                speak('congratulations    file written succesfully')
            except Exception as e:
                print(e)
                speak("sorry something went wrong")
