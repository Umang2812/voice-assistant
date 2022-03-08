#from socket import J1939_NLA_BYTES_ACKED
import speech_recognition as sr #convert speech to text
#import datetime #for fetching date and time
from datetime import datetime
import wikipedia
import webbrowser
import requests
import playsound # to play saved mp3 file 
import winsound
from gtts import gTTS # google text to speech 
import os # to save/open files 
import time
import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations
import pyttsx3
import smtplib
import pyjokes
import subprocess
import wolframalpha
from flask import Flask
#import email_sender
import pyttsx3
import os
import smtplib
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
#import feedparser
import smtplib
import ctypes
import time
import requests
from urllib.request import urlopen
from email.message import EmailMessage
import shutil
from tkinter import *

from tkinter import filedialog
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
#from twilio.rest import Client
#from clint.textui import progress
#from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import mysql.connector

#mycursor.execute("CREATE TABLE voiceassistant (command varchar(255), results VARCHAR(255))")
#mycursor.execute("ALTER TABLE voiceassistant ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

class inflow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\chromedriver')

    def get_info(self, query):
        self.query = query
        self.driver.get(url = "https://www.wikipedia.org")

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
    speak('Hello , I am Friday, your Artificial intelligence assistant. Please tell me how may I help you')
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
def set_time():
    
    while True:
        settime = f"{hour.get()}:{min.get()}:{sec.get()}"
        print(settime)
       # speak("Enter hour")
        #hr = str(input("Enter hour in 24 hr format"))
        #speak("Enter minutes")
       # min = str(input("Enter min "))
        #speak("Enter second")
       # sec = str(input("Enter sec"))
       # settime = " "+hr+":"+min+":"+sec
        settime = str(settime)
        validate = validate_time(settime)
        if validate != "ok":
            print(validate)
        else:
            print(f"Setting alarm for {settime}...")
            break
    return settime
def set_date():
    while True:
        setdate = f"{month.get()}/{day.get()}/{year.get()}"
        print(setdate)
        setdate = str(setdate)
        validate = validate_date(setdate)
        if validate != "ok":
            print(validate)
        else:
            print(f"Setting alarm for {setdate}...")
            break
    return setdate
    
def validate_date(alarm_date):
    if len(alarm_date) !=8:
        speak("Invalid date format! Please try again...")
        return "Invalid date format! Please try again..."
    else:
        
        if int(alarm_date[3:5]) > 31:
            speak("Invalid day format! Please try again...")
            return ("Invalid day format! Please try again...")
        elif int(alarm_date[0:2]) > 12:
            speak("Invalid MONTH format! Please try again...")
            return "Invalid MONTH format! Please try again..."
        elif int(alarm_date[6:8]) > 100:
            speak("Invalid YEAR format! Please try again...")
            return "Invalid YEAR format! Please try again..."
        else:
            speak("ok")
            return "ok"
   

#time_set = set_time()
#date_set = set_date()

#print(time_set, date_set)

#print(type(time_set),type(date_set))
def validate_time(alarm_time):
    if len(alarm_time) !=8:
        a = speak("Invalid time format! Please try again...")
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 24:
            b = speak("Invalid HOUR format! Please try again...")
            return ("Invalid HOUR format! Please try again...")
        elif int(alarm_time[3:5]) > 59:
            c = speak("Invalid MINUTE format! Please try again...")
            return "Invalid MINUTE format! Please try again..."
        elif int(alarm_time[6:8]) > 59:
            d = speak("Invalid SECOND format! Please try again...")
            return "Invalid SECOND format! Please try again..."
        else:
            e = speak("ok")
            return "ok"

        
def Alarm():
    time_set = set_time()
    while True:
        
        now = datetime.datetime.now()
        current_hour = now.strftime("%H")
        current_min = now.strftime("%M")
        current_sec = now.strftime("%S")
        if time_set[0:2] == current_hour:
                
                if time_set[3:5] == current_min:
                    
                    if time_set[6:8] == current_sec:
                        return True
                        
def Cal():
    date_set = set_date()
    while True:
        now = datetime.datetime.now()
        if date_set == now.strftime("%x"):
            return True
def final_Alarm():
    while True:
        alarm = Alarm()
        cal = Cal()
        if alarm ==True and cal ==True:
            print("Wake Up!")
                        
            music_dir = 'D:\\pythonproject\\alarm.wav'
            mesg = f"{msg.get()}"
            print(mesg)
            speak(mesg)
            
            os.startfile(music_dir)
            break

EMAIL_ADDRESS = os.environ.get('USER_EMAIL')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS_2')
def server_login():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    text =msg.as_string()
    server.sendmail(EMAIL_ADDRESS,  msg['To'], text)
    server.quit()
#import modules
 
from tkinter import *
import os
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
    login_screen.destroy()
    main_screen.destroy()
    
    
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 


if __name__=="__main__" :  
    main_account_screen()
     
    wishMe()
    query_list = []
    date_list = []
    time_list = []
    while True:
        query = takeCommand().lower() #Converting user query into lower case        
            # Logic for executing tasks based on query
        now = datetime.datetime.now()
        query_list.append(query)
        date_list.append(now.strftime("%x"))
        time_list.append(now.strftime("%H:%M:%S"))
        # time_list.append(now.strftime("%H:%M:%S"))
        
        
        if query==0:
            continue
            
        if "stop" in str(query) or "exit" in str(query) or "bye" in str(query) or "close" in str(query):
            speak("Bye and see you soon")
            mydb = mysql.connector.connect(host="localhost", user = "root", passwd = "umang", database= "db1")
            mycursor = mydb.cursor()    
            # mycursor.execute("CREATE TABLE voice (command varchar(255), dates VARCHAR(255), time_of_execution VARCHAR(255))")
            sql = "INSERT INTO voice (command, dates, time_of_execution) VALUES (%s, %s, %s)" 
            val = []  
            for i in range(len(query_list)):
                val.append([query_list[i],date_list[i],time_list[i]])
            mycursor.executemany(sql, val)

            mydb.commit()  
            break
        
        elif "facebook" in str(query):
            speak("Opening facebook")
            webbrowser.open("facebook.com")
        elif "linkedin" in query:
            speak("Opening linkedin")
            webbrowser.open("linkedin.com")
            
            
        elif 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:

            music_dir = 'C:\\Users\\Admin\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[1]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif "open word" in query: 
            speak("Opening Microsoft Word") 
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word') 
        elif "open excel" in query: 
            speak("Opening Microsoft Word") 
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel') 
        elif "weather" in query:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            print(city_name)
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                        str(current_temperature) +
                        "\n humidity in percentage is " +
                        str(current_humidiy) +
                        "\n description  " +
                        str(weather_description))
                print(" Temperature in kelvin unit = " +
                        str(current_temperature) +
                        "\n humidity (in percentage) = " +
                        str(current_humidiy) +
                        "\n description = " +
                        str(weather_description))

            else:
                speak(" City Not Found ")
        #elif "camera" in query or "take a photo" in query:
            #       ec.capture(0, "Jarvis Camera ", "img.jpg")
        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                    
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        elif"where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            print(location)
            webbrowser.open("https://www.google.nl/maps/place/" + location + "")

        
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
                
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
            
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))
        elif query == "email":
            EMAIL_ADDRESS = os.environ.get('USER_EMAIL')
            EMAIL_PASSWORD = os.environ.get('EMAIL_PASS_2')
            speak("Whom would you like to send this email to")
            speak("Please type the username")
            user_name = input("Sender Username")
            speak("Say your subject")
            subject = takeCommand()
            speak("Say your message")
            message = takeCommand()
            #file_location = 'C:\\Users\\You\\Desktop\\attach.txt'
            
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = user_name +"@gmail.com"
            msg['Subject'] = subject
            speak('Would you like to attach any attachment? Respond with yes or no')
            res = takeCommand().lower()
            if res =="yes":
                speak("Please select your file")
                filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Admin\\Desktop",title="Open file okay?"
                                            ,filetypes= (("text files","*.txt"),('img','*.jpg'),('Python Files','*.py'),('Docx files','*.docx')    
                                                        ,("all files","*.*")))
                file = open(filepath,'rb')
                #image_type = imghdr.what(filepath.name)
                file_data = file.read()
                file.close()


                msg.attach(MIMEText(message, 'plain'))

                # Setup the attachment
                filename = os.path.basename(filepath)
                attachment = open(filepath, "rb")
                
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                # Attach the attachment to the MIMEMultipart object
                msg.attach(part)
                server_login()
            else:
                server_login()
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
        elif "alarm" in query:
            clock = Tk()
            clock.title("Hope you are having a good day")
            clock.geometry("500x700")
            clock.configure(background="blue")
            time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
            addTime = Label(clock,text = "Hour    Min    Sec",font=30).place(x = 110)
            setYourAlarm = Label(clock,text = "Set time",fg="green",relief = "solid",font=("Helevetica",15,"bold")).place(x=0, y=29)
            # The Variables we require to set the alarm(initialization):
            hour = StringVar()
            min = StringVar()
            sec = StringVar()
            #Time required to set the alarm clock:
            hourTime= Entry(clock,textvariable = hour,bg = "white",width = 10).place(x=110,y=60)
            minTime= Entry(clock,textvariable = min,bg = "white",width = 10).place(x=170,y=60)
            secTime = Entry(clock,textvariable = sec,bg = "white",width = 10).place(x=230,y=60)
            date_format=Label(clock, text= "Enter date in DD/MM/YY format!", fg="red",bg="black",font="Arial").place(x=60,y=310)
            adddate = Label(clock,text = "Day   Month   Year",font=30).place(x = 110,y =210)
            setYourDate = Label(clock,text = "Date",fg="green",relief = "solid",font=("Helevetica",10,"bold")).place(x=0, y=218)
            day = StringVar()
            month = StringVar()
            year = StringVar()
            msg = StringVar()
            #To take the time input by user:
            #submit = Button(clock,text = "Set time",fg="red",width = 10,command = Alarm).place(x =110,y=70)
            
            dayno= Entry(clock,textvariable = day,bg = "white",width = 10).place(x=110,y=240)
            monthno= Entry(clock,textvariable = month,bg = "white",width = 10).place(x=170,y=240)
            yearno = Entry(clock,textvariable = year,bg = "white",width = 10).place(x=230,y=240)
            #To take the time input by user:
            #submit2 = Button(clock,text = "Set date",fg="red",width = 10,command = Cal).place(x =110,y=170)En
            setYourAlarm = Label(clock,text = "Message",fg="green",relief = "solid",font=("Helevetica",15,"bold")).place(x=0, y=370)
            messagebox = Entry(clock,textvariable = msg,bg = "white",width = 40).place(x=110,y=370)
            
            submit3 = Button(clock,text = "Set Alarm",fg="red",width = 30,command = final_Alarm).place(x =90,y=500)
            
                
            clock.mainloop()
        
                    
        else:
            speak("We are sorry!Can you repeat what you said")

            

                
