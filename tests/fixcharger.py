#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)

print "Fixing shit"
GPIO.output(12,GPIO.HIGH)
GPIO.cleanup()


