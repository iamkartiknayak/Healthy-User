from playsound import playsound
import speech_recognition as sr
from datetime import datetime
from time import time, sleep
from gtts import gTTS
from random import choice
import os


def listen(cmd, flag):
    '''This function will listen to user for appropriate reply for the same asked by program'''
    drank_water = ["I drank water", "I drink water", "I drank some water", "I drink some water"]
    eye_exercise = ["I did eyes exercise", "I exercise my eyes"]
    physical_exercise = ["I walked", "I did walk", "I did physical exercise", "I did physical activity"]
    crt_time = time()
    while True:
        time_interval = time()
        if time_interval - crt_time >= 60*5:
            remind(cmd, flag)
        else:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.pause_threshold = 1
                audio = r.listen(source)
            try:
                text = ""
                text = r.recognize_google(audio,language='en')
            except:
                pass
            print(f"flag:{flag}\nUser said:{text}")
            if flag == "water" and text in drank_water:
                log_record(flag)
                break
            elif flag == "eyes" and text in eye_exercise:
                log_record(flag)
                break
            elif flag == "physical" and text in physical_exercise:
                log_record(flag)
                break
            else:
                pass
            sleep(0.1)


def get_username():
    '''This function will get the user name'''
    for user, name in os.environ.items():
        if user == "USERNAME":
            return name

def log_record(flag):
    '''This funtion will create a text file containing user data with respect to when he drink water or did he exercise his body or relax his eyes from the screen'''
    name = get_username()
    time_stamp = datetime.now().strftime("%H:%M:%S")
    with open("/home/"+name+"/Documents/Log file.txt",'a') as log_file:
        log_file.write(f"{flag} at {time_stamp}\n")


def remind(cmd, flag):
    '''This function will remind user again if he doesn't reply within 5 minutes from when the program asked the question'''
    speak(cmd,flag)


def speak(cmd,flag):
    '''This function will tell user to do ceratin things from To-do list'''
    tts = gTTS(text=cmd, slow=False)
    file_name = "temp.mp3"
    tts.save(file_name)
    playsound(file_name)
    os.remove(file_name)
    listen(cmd, flag)


def main():
    '''This is main function which is responsible for running all other servcies''' 
    water_time = eyes_time = physical_time = time()
    while True:
        current_time = time()
        if current_time - water_time > 20 * 60:
            flag = "water"
            speak(choice(water), flag)
            water_time = time()

        if current_time - eyes_time > 15 * 60:
            flag = "eyes"
            speak(choice(eyes), flag)
            eyes_time = time()

        if current_time - physical_time > 40 * 60:
            flag = "physical"
            speak(choice(physical), flag)
            physical_time = time()
        sleep(0.1)


if __name__ == "__main__":
    start_time = datetime.now().strftime("%H:%M:%S")
    water = ["It's been a while drink some water", "You should drink some water"]
    eyes = ["You should probably take some rest from the screen", "Close your eyes and relax for a bit"]
    physical = ["It's been a while do some physical activity", "Take some leisure time from the device and walk a bit"]
    main()
