#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print("-------------")
print(" Motor + GPIO ")
print("-------------")

Motor1A = 12
Motor1B = 22
Motor1E = 27
delay = 2

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

print("Turning motor on backwards!")
GPIO.output(Motor1A, GPIO.HIGH)
GPIO.output(Motor1B, GPIO.LOW)
GPIO.output(Motor1E, GPIO.HIGH)

sleep(delay)

print("Stopping motor")
GPIO.output(Motor1E, GPIO.LOW)

print("Turning motor on forwards!")
GPIO.output(Motor1A, GPIO.LOW)
GPIO.output(Motor1B, GPIO.HIGH)
GPIO.output(Motor1E, GPIO.HIGH)

sleep(delay)

print("Stopping motor")
GPIO.output(Motor1E, GPIO.LOW)

GPIO.cleanup()
