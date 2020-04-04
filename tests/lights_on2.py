#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

gpio = input("Enter GPIO: ")

GPIO.setup(gpio,GPIO.OUT)
print "Lights on madafaka! GPIO = " + str(gpio)
GPIO.output(gpio,GPIO.HIGH)
time.sleep(2)
print "Lights out madafaka!"
GPIO.output(gpio,GPIO.LOW)
