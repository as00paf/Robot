#!/usr/bin/python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(17,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
print "Lights out sucka!"
GPIO.output(17,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
GPIO.output(27,GPIO.LOW)

