#!/usr/bin/env python3

import time, json, socket, queue, os, threading, gtts

import speech_recognition as sr

waitingForConf = False
lastQuestion = None

readyToReceive = False

triggerWord = 'Jean-marie'

sock = None

def callback(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language="fr-FR")
        print("Google Speech Recognition thinks you said : " + text)

        handleSentence(text)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))





def handleSentence(text):
    global lastQuestion, readyToReceive, sock
    if triggerWord in text.split(' ', 1)[0]: # trigger sur premier mot
        text = text.partition(' ')[2] # delete du trigger
        js = None
        if not waitingForConf or lastQuestion is None:
            js = json.dumps({'type': 'question', 'msg': text, 'answer': ''})
            lastQuestion = text
        else:
            js = json.dumps({'type': 'question', 'msg': lastQuestion, 'answer': text})

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setblocking(True)
        sock.settimeout(None)
        sock.connect(('localhost', 15555))
        sock.send(str.encode(js))
        readyToReceive = True

def speechThread():
    global readyToReceive, sock

    r = sr.Recognizer()
    r.energy_threshold = 4000
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source)

    stop_listening = r.listen_in_background(m, callback)

    while 42:
        if readyToReceive:
            text = json.loads(sock.recv(1024).decode('utf-8'))
            sock.close()
            if text:
                print("received", text['msg'])
                stop_listening(wait_for_stop=False)
                tts = gtts.gTTS(text=text['msg'], lang='fr')
                tts.save("text.mp3")
                os.system("mplayer text.mp3 1> /dev/null 2> /dev/null")
                os.remove("text.mp3")
                stop_listening = r.listen_in_background(m, callback)
                readyToReceive = False
        time.sleep(0.1)




t = threading.Thread(target=speechThread)
t.start()

while True: time.sleep(0.1)
