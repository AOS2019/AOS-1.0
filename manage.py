# NOTE: This requires PyAudio since it makes use of the Microphone class

######cleaning  search request

import speech_recognition as sr
import pyttsx3
import pyjokes
import wikipedia
import re
import os
import datetime
import webbrowser
import requests
# import Main_Window



##USER class

#ouputs response
def response(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

#response("How can I assist you today?")
#obtain audio from the microphone

r = sr.Recognizer()
def command():
    with sr.Microphone() as source:
        audio = r.listen(source)
        response("am listening")
        query = ''
        #conn = requests.get('https://www.google.com/').status_code
        #recognize_sphinx(audio) --offline
        #recognize_google(audio) --online
        try:
            query = "You said " + r.recognize_sphinx(audio).lower() + "."
            response(query)
            #reply(query)
        except sr.UnknownValueError:
            response("Sorry, I couldn't understand that")
        except sr.RequestError:
            response("Sorry, my speech service is down")
        return query
        #if conn == 200:
            # recognize speech using speech recognizer
        #    response("Connecting to the internet")
            #response("You need an internet connection for this!")
        #    query = "You said " + r.recognize_google(audio).lower() + "."
        #    response(query)
        #else:
            # recognize speech using Sphinx
        #    query = "You said " + r.recognize_sphinx(audio).lower() + "."
        #    response(query)
            #print(query)
        #    if sr.UnknownValueError:
        #        response("Sorry, I couldn't understand that")
        #    elif sr.RequestError:
        #        response("Sorry, my speech service is down")
        #return query
        
                        
##TASK class

#play music function
def Play_Music():
    music_dir = 'C:\\Users\\mitchel\\Music'
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir, songs[0]))
    
#Tell a joke function
def Tell_Joke(lang='en', cat='neutral'):
    joke = pyjokes.get_joke(language=lang, category=cat)
    response(joke)
    
#Tell time
def Tell_time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    response(f"The time is {strTime}")

##QUERY class




#interpret response
def reply(query):
    if "what is your name" in query:
        response("My name is AOS  1.0, Your virtual assistant.")
    elif "play music" in query:
        Play_Music()
    elif "joke" in query:
        Tell_Joke()
    elif "what is the time" in query:
        Tell_time()
    elif "what is" in query:
        response("You need an internet connection for this!")
        try:
            res = wikipedia.summary(query, sentences = 3)
            res = re.sub('[^a-zA-Z.\d\s]', ' ', res)[1:]
        except ConnectionError:
            response("Sorry, my speech service is down")
        response(res)
    elif "search" in query:
        response("You need an internet connection for this!")
        query = str(query)
        search = query.replace(str("seach for"), str(""))
        url = "https://google.com/search?q=" + search
        webbrowser.get().open(url)
        response("Here is what I found for" + search)
    elif "youtube" in query:
        response("You need an internet connection for this!")
        webbrowser.open("https://www.youtube.com/playlist")
    elif "about" in query:
        ui = Main_Window.Ui_MainWindow_main()
        ui.aboutWindow()
    elif "help" in query:
        ui = Main_Window.Ui_MainWindow_main()
        ui.helpWindow()
    elif "voice" in query:
        ui = Main_Window.Ui_MainWindow_main()
        ui.voiceWindow()
    elif "exit" in query:
        exit() 


#query = command()
#reply(query)
