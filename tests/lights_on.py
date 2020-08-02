#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
light = 19
GPIO.setup(light,GPIO.OUT)
#GPIO.setup(18,GPIO.OUT)
#GPIO.setup(27,GPIO.OUT)

print "Lights on madafaka!"
GPIO.output(light,GPIO.HIGH)
#GPIO.output(18,GPIO.HIGH)
#GPIO.output(27,GPIO.HIGH)



