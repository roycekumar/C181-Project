from tkinter import *
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import subprocess
import webbrowser
root=Tk()
root.geometry("500x500")
root.configure(bg="Light Blue")
label=Label(root,text="Welcome To Your Personal Desktop Assistant",bg="Light Blue",font=("Bahnschrift Light",15,"bold"))
label.place(relx=0.5,rely=0.1,anchor=CENTER)
text_to_speech=pyttsx3.init()
Label_speak=Label(root,font=("Arial",30,"bold"),bg="Light Blue")
Label_speak.place(relx=0.5,rely=0.7,anchor=CENTER)
def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()
def r_audio():
    speak("How can I help you?")
    speech_recognisor=sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now")
        audio=speech_recognisor.listen(source)
        voice_data=''
        try: 
            voice_data=speech_recognisor.recognize_google(audio,language="en-in")
        except:
            speak("Please repeat")
    respond(voice_data)
def respond(voice_data):
    voice_data=voice_data.lower()
    print(voice_data)
    if "name" in voice_data:
        speak("My name is Royce's Personal Assisstant")
        print("My name is Royce's Personal Assisstant")
    if "time" in voice_data:
        now=datetime.now()
        current_time=now.strftime("%H:%M:%S")
        speak("Current Time is "+current_time)
        print("Current Time is "+current_time)
    if "day" in voice_data:
        day=datetime.now()
        day=day.strftime("%A")
        speak("Today is "+day)
        print("Today is "+day)
    if "search" in voice_data:
        speak("Opening Google")
        print("Opening Google")
        webbrowser.get().open("https://google.com/")
    if "youtube" in voice_data:
        speak("Opening Youtube")
        print("Opening Youtube")
        webbrowser.get().open("https://youtube.com/")
    if "text editor" in voice_data or "notepad" in voice_data:
        speak("Opening Notepad")
        print("Opening Notepad")
        subprocess.Popen(["notepad.exe"])
    if "excel" in voice_data:
        speak("Opening Microsoft Excel")
        print("Opening Microsoft Excel")
        subprocess.Popen(["Excel.exe"])
    if "word" in voice_data:
        speak("Opening Microsoft Word")
        print("Opening Microsoft Word")
        subprocess.Popen(["WINWORD.EXE"])
    if "powerpoint" in voice_data:
        speak("Opening Microsoft PowerPoint")
        print("Opening Microsoft PowerPoint")
        subprocess.Popen(["POWERPNT.EXE"])
btn=Button(root,text="Start",bg="red3",fg="white",padx=10,pady=1,font=("Arial",11,"bold"),relief=FLAT,command=r_audio)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()
