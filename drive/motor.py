#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

class Motor:

    def __init__(self, ma, mb, me):
        self.ma = ma
        self.mb = mb
        self.me = me

        GPIO.setup(M1A, GPIO.OUT)
        GPIO.setup(M1B, GPIO.OUT)
        GPIO.setup(M1E, GPIO.OUT)


    def goForward():
        print("Going forward!")
        
        GPIO.output(ma, GPIO.HIGH)
        GPIO.output(mb, GPIO.LOW)
        GPIO.output(me, GPIO.HIGH)

    def goForward(duration):
        print("Going forward for " + duration + " seconds")
        goForward()
        sleep(duration)
        stop()

    def stop():
        print("Stopping")
        
        GPIO.output(me, GPIO.LOW)
