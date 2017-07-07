#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

print "Lights on madafaka!"

GPIO.output(17,GPIO.HIGH)
time.sleep(3)
GPIO.output(17,GPIO.LOW)

time.sleep(1)

GPIO.output(27,GPIO.HIGH)
time.sleep(3)
GPIO.output(27,GPIO.LOW)
GPIO.cleanup()

