#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
#GPIO.setup(18,GPIO.OUT)
#GPIO.setup(27,GPIO.OUT)

print "Lights on madafaka!"
GPIO.output(17,GPIO.HIGH)
#GPIO.output(18,GPIO.HIGH)
#GPIO.output(27,GPIO.HIGH)



