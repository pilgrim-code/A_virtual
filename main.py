from genericpath import exists
import pyttsx3 
import speech_recognition as sr 
import datetime
import webbrowser
import os
import smtplib
import json
import pyautogui

#import tensorflow as tf
opera_path = r"C://Users//Pilgrim//AppData//Local//Programs//Opera GX//opera.exe"
webbrowser.register('opera',None,webbrowser.BackgroundBrowser(opera_path),preferred=True)
programas_registrados = [] #Lectura
programas_to_json = [] #Escritura


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
def escritura_json(programas_to_json):
    with open("Programas.json", "w") as j:
                    json.dump(programas_to_json,j)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Inicio():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Buenos dias!")

    elif hour>=12 and hour<18:
        speak("Buenas tardes!")   

    else:
        speak("Buenas noches!")  

    speak("Soy tu asistente dime un comando para ayudarte!")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='es-ES')
        speak(f"Dijo: {query}\n")
        print(f"FLAG {query}\n")
        if query == "arroba":
            query = "@"+""
            print(query)

    except Exception as e:
        # print(e)    
        speak("Intenta nuevamente...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def busqueda_navegador(query):
    
    speak("Que busqueda deseas hacer?")
    query = takeCommand().lower()
    if 'abrir youtube' in query:
        webbrowser.get('opera').open("youtube.com")
        
    elif 'abrir historial youtube' in query:
        webbrowser.get('opera').open("youtube.com/feed/history")

    elif 'busca mis monas chinas' in query:
        webbrowser.get('opera').open("https://www1.otakustv.com")
    elif 'busca' in query:
            speak("Que busco?")
            query=webbrowser.get('opera').open(takeCommand()) 
    elif 'cerrar ventana' in query:
        speak("Cerrando ventana")
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('w')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('w')

    
    
def abrir_programa(query):
    
    with open("Programas.json","r") as k:
        programas =json.load(k)
        print(programas)
    speak(f"Que programa quieres abrir? Tengo registrados : {programas}")
    query = takeCommand().lower()
    if 'visual' in query:
            codePath = "C:/Users/Pilgrim/AppData/Local/Programs/Microsoft VS Code/Code.exe"
            os.startfile(codePath)
            programas_to_json.append(query)
            print(programas_to_json)
            escritura_json(programas_to_json)
            

    elif 'word' in query:
        codePath = "C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE"
        os.startfile(codePath)
        programas_to_json.append(query)
        print(programas_to_json)
        escritura_json(programas_to_json)
        
    elif 'ppt' in query:
        codePath = "C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE"
        os.startfile(codePath)
        programas_to_json.append(query)
        print(programas_to_json)
        escritura_json(programas_to_json)

    elif 'whatsapp' in query:
        print(query)
        #programas_registrados.append(query)
        programas_to_json.append(query)
        print(programas_registrados)
        codePath = "C:/Users/Pilgrim/AppData/Local/WhatsApp/WhatsApp.exe"
        os.startfile(codePath)
        print(programas_to_json)
        escritura_json(programas_to_json)

if __name__ == "__main__":
    Inicio()
    while True:
   
        query = takeCommand().lower()

        # Logic for executing tasks based on query
     
        if 'abrir navegador' in query:
            busqueda_navegador(query)

        elif 'que hora es' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Señor, la hora es {strTime} ")

        if 'abrir programa' in query:
            abrir_programa(query)
        
        elif 'mensaje a big data' in query:
            try:
                speak("que le digo?")
                content = takeCommand()

                
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")    
