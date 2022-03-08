from selenium import webdriver # to control browser operations
import speech_recognition as sr #convert speech to text
import datetime #for fetching date and time
import wikipedia
import webbrowser
import requests
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
import time
import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations
import pyttsx3
import smtplib

class inflow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\Users\Admin\Downloads\chromedriver.exe')

    def get_info(self, query):
        self.query = query
        self.driver.get(url = "https://www.wikipedia.org")
assist = inflow()
assist.get_info("hello")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') #gets you the details of the current voice
engine.setProperty('voice', voices[1].id)  # 0-male voice , 1-female voice

def speak(audio):   
    engine.say(audio)    
    engine.runAndWait() #Without this command, speech will not be audible to us.
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")    
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")       
    
    else:
        speak("Good Evening!")      
    speak('Hello Sir, I am Friday, your Artificial intelligence assistant. Please tell me how may I help you')
def takeCommand():
    #It takes microphone input from the user and returns string output    
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.    
    except Exception as e:
        # print(e)  use only if you want to print the error!
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query