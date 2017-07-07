#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
GPIO.cleanup()
sleep(3)

print("-------------")
print(" Motor + GPIO ")
print("-------------")

#Motor1E = vert = 27-22
#Motor1B = bleu = 18-18
#Motor1A = jaune = 17-16

#Motor2A = bleu = 13-23
#Motor2B = jaune = 19-21
#Motor2E = vert = 26-19

Motor1A = 17
Motor1B = 18
Motor1E = 27

Motor2A = 13
Motor2B = 19
Motor2E = 26

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)

print("Turning motor on!")
GPIO.output(Motor1A, GPIO.HIGH)
GPIO.output(Motor1B, GPIO.LOW)
GPIO.output(Motor1E, GPIO.HIGH)

sleep(5)

print("Stopping motor")
GPIO.output(Motor1E, GPIO.LOW)

print("Turning second motor on!")
GPIO.output(Motor2A, GPIO.HIGH)
GPIO.output(Motor2B, GPIO.LOW)
GPIO.output(Motor2E, GPIO.HIGH)

sleep(5)

print("Stopping second motor")
GPIO.output(Motor2E, GPIO.LOW)


print("Going backwards!")
GPIO.output(Motor1A, GPIO.LOW)
GPIO.output(Motor1B, GPIO.HIGH)
GPIO.output(Motor1E, GPIO.HIGH)

sleep(5)

print("Stopping motor")
GPIO.output(Motor1E, GPIO.LOW)

GPIO.cleanup()

            
