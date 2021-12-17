#!/usr/bin/env python3

import speech_recognition as sr
import cv2
import time
import words as KEY

from CommandHandler import CommandHandler
from MachineState import State

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

def main():
    stop_program_flag = True;
    
    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        print ('Calibrating microphone..')
        r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
        print ('Calibration succeed')
    # start listening in the background (note that we don't have to do this inside a `with` statement)
    stop_listening = r.listen_in_background(m, callback)
    
    #in paralel run the logic of application
    machineState = State()
    while stop_program_flag:
        time.sleep(0.1)
        stop_program_flag = machineState.update(CH.getLastCommand())
        print (CH.command_dic)
        

    # calling this function requests that the background listener stop listening
    stop_listening(wait_for_stop=False) 
    
    
    #TODO Check for active microphone, use sr.Microphone.list_microphone_names()?!
    # TODO: handle unconected camera:D
    #    VIDEOIO ERROR: V4L: can't open camera by index 0
    #        Traceback (most recent call last):
    #        File "main.py", line 38, in <module>
    #            take_photo()
    #        File "main.py", line 14, in take_photo
    #            cv2.imshow('Imagetest',image)
    #        cv2.error: OpenCV(4.1.0) /home/pi/opencv-python/opencv/modules/highgui/src/window.cpp:352: error: (-215:Assertion failed) size.width>0 && size.height>0 in function 'imshow'

if __name__ == "__main__":
    main()


