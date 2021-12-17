#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import time
import cv2
import speech_recognition as sr

from CommandHandler import CommandHandler
from MachineState import State
import words as KEY


CH = CommandHandler(KEY.commands_list)

# this is called from the background thread
def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        test_val = recognizer.recognize_google(audio)
        CH.update(test_val)
        print("You said " + test_val)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

def take_photo():
    cam = cv2.VideoCapture(0)
    while True:
        cnt=0;
        ret, image = cam.read()
        cv2.imshow('Imagetest',image)
        key = cv2.waitKey(27)
        if (key == 32): #press 'space' to take the photo
            cnt=cnt +1
            cv2.imwrite('/home/pi/Desktop/SoundRecon/images/testimage' +str(cnt) + ".jpg", image)
        elif (key == 113): #press 'q' to quit the window
            break
    cam.release()
    cv2.destroyAllWindows()
    
r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    print ('Calibrating microphone..')
    r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
    print ('Calibration succeed')
# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)

# do some unrelated computations for 5 seconds
take_photo()
    


# calling this function requests that the background listener stop listening
stop_listening(wait_for_stop=False)
print ("End!!")
# do some more unrelated things

