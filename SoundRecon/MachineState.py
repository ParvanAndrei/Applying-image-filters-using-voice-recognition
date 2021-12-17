#!/usr/bin/env python3
import cv2
import words as KEY
import os
import TakePhoto as photo
import MedianFilter
import GaussianFilter
from lcd import drivers
from time import sleep
#from datetime import datetimey

#/*******************************************
#
#*******************************************/
#internal states
display = drivers.Lcd()

STATE_INIT = 1
STATE_PHOTO = 2
STATE_CLOSE = 3
STATE_EXIT = 4
STATE_MEDIAN = 5
STATE_GAUSSIAN = 6


#Regula! in diagrama de comanda niciodata intrarea nintr-o satre sa nu fie egala cu ale intrari sau iesiri
class State(object):
    actual_state = STATE_INIT

    def __init__(self):
        self.actual_state = STATE_INIT
        
#/******************************************************************
#   This function will return False when the aplication should stop
#******************************************************************/
    def update(self, command):
        if command == KEY.MAKE_PHOTO: 
            self.make_photo_tranzition(command)
        elif command == KEY.CLOSE_WINDOW:
            self.close_tranzition(command)
        elif command == KEY.MEDIAN_FILTER:
            self.median_filter_tranzition(command)
        elif command == KEY.GAUSSIAN_FILTER:
            self.gaussian_filter_tranzition(command)
        elif command == KEY.STOP_PROGRAM:
            print ("EXIT state")
            display.lcd_clear()
            display.lcd_display_string("Bye bye", 1)
            sleep(2)
            display.lcd_clear()
            return False
        return True

    def make_photo_tranzition(self, command):
        if self.actual_state == STATE_INIT:
            self.actual_state = STATE_PHOTO
            #os.system("raspistill -o testimg.jpg")
            display.lcd_clear()
            display.lcd_display_string("Photo state", 1)
            display.lcd_display_string("Smile",2)
            photo.take_photo()
            print ("Photo state")
        return True
    def median_filter_tranzition(self,command):
        if self.actual_state == STATE_INIT:
            self.actual_state = STATE_MEDIAN
            print("Median filter state")
            display.lcd_clear()
            display.lcd_display_string("Median", 1)
            MedianFilter.main()
            #print("Median filter state")
        return True

    def gaussian_filter_tranzition(self, command):
        if self.actual_state == STATE_INIT:
            self.actual_state = STATE_GAUSSIAN
            print("Gaussian filter state")
            display.lcd_clear()
            display.lcd_display_string("Gaussian", 1)
            GaussianFilter.main()
        return True
    def close_tranzition(self, command):
        if self.actual_state == STATE_PHOTO:
            self.actual_state = STATE_INIT
#            cv2.waitKey(0)
#            cv2.destroyAllWindows()
            display.lcd_clear()
            display.lcd_display_string("Choose state", 1)
            print ("INIT state")
        elif self.actual_state == STATE_MEDIAN:
            self.actual_state = STATE_INIT
            cv2.destroyAllWindows()
            display.lcd_clear()
            display.lcd_display_string("Choose state", 1)
            print ("INIT state")
        elif self.actual_state == STATE_GAUSSIAN:
            self.actual_state = STATE_INIT
            cv2.destroyAllWindows()
            display.lcd_clear()
            display.lcd_display_string("Choose state", 1)
            print ("INIT state")

        return True
