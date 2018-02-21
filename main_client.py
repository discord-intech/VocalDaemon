#!/usr/bin/env python3

import time, json, socket, queue, os, threading

import speech_recognition as sr

waitingForConf = False
lastQuestion = None

triggerWord = 'saucisse'

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setblocking(True)
socket.settimeout(None)
socket.connect(('localhost', 15555))
speechQueue = queue.Queue()

def handleSentence(text):
    global lastQuestion
    if triggerWord in text:
        js = None
        if not waitingForConf or lastQuestion is None:
            js = json.dumps({'type': 'question', 'msg': text, 'answer': ''})
            lastQuestion = text
        else:
            js = json.dumps({'type': 'question', 'msg': lastQuestion, 'answer': text})

        socket.send(str.encode(js))

def speechThread():

    while 42:
        text = socket.recv(1024).decode('utf-8')
        if text:
            command = "espeak \"" + text + "\" -v fr -s 140 1> /dev/null 2> /dev/null"
            os.system(command)
        time.sleep(0.1)

def callback(recognizer, audio):
    try:

        text = recognizer.recognize_google(audio, language="fr-FR")
        print("Google Speech Recognition thinks you said : " + text)

        handleSentence(text)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


r = sr.Recognizer()
r.energy_threshold = 1000
m = sr.Microphone()
with m as source:
    r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(m, callback)

t = threading.Thread(target=speechThread)
t.start()

while True: time.sleep(0.1)
