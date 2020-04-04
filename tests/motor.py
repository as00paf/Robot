#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

print("-------------")
print(" Motor + GPIO ")
print("-------------")

#26-19-13
#Motor1B = mauve-bleu = 17
#Motor1E = orange-mauve = 27
#Motor1A = bleu-blanc = 22

#6-5-12
#Motor2A = vert-bleu = 21
#Motor2B = orange-mauve = 20
#Motor2E = mauve-blanc = 16

#17-27-22
#Motor3A = vert-blanc = 26
#Motor3B = blanc-mauve = 19
#Motor3E = jaune-bleu = 13

#23-24-25
#Motor4A = gris-blanc = 5
#Motor4B = mauve-mauve = 6
#Motor4E = bleu-bleu = 12

Motor1A = 22
Motor1B = 17
Motor1E = 27

Motor2A = 21
Motor2B = 20
Motor2E = 16

Motor3A = 26
Motor3B = 13
Motor3E = 19

Motor4A = 5
Motor4B = 6
Motor4E = 12

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)

GPIO.setup(Motor3A, GPIO.OUT)
GPIO.setup(Motor3B, GPIO.OUT)
GPIO.setup(Motor3E, GPIO.OUT)

GPIO.setup(Motor4A, GPIO.OUT)
GPIO.setup(Motor4B, GPIO.OUT)
GPIO.setup(Motor4E, GPIO.OUT)

#Motor1

print("Turning motor on backwards!")
GPIO.output(Motor1A, GPIO.HIGH)
GPIO.output(Motor1B, GPIO.LOW)
GPIO.output(Motor1E, GPIO.HIGH)

sleep(1)

print("Stopping motor")
GPIO.output(Motor1E, GPIO.LOW)

print("Turning motor on forwards!")
GPIO.output(Motor1A, GPIO.LOW)
GPIO.output(Motor1B, GPIO.HIGH)
GPIO.output(Motor1E, GPIO.HIGH)

sleep(1)

print("Stopping motor")
GPIO.output(Motor1E, GPIO.LOW)

#Motor2
print("Going forward!")
GPIO.output(Motor2A, GPIO.HIGH)
GPIO.output(Motor2B, GPIO.LOW)
GPIO.output(Motor2E, GPIO.HIGH)

sleep(1)

print("Stopping motor")
GPIO.output(Motor2E, GPIO.LOW)


print("Going backwards!")
GPIO.output(Motor2A, GPIO.LOW)
GPIO.output(Motor2B, GPIO.HIGH)
GPIO.output(Motor2E, GPIO.HIGH)

sleep(1)

print("Stopping motor")
GPIO.output(Motor2E, GPIO.LOW)

#Motor3
print("Going forward!")
GPIO.output(Motor3A, GPIO.HIGH)
GPIO.output(Motor3B, GPIO.LOW)
GPIO.output(Motor3E, GPIO.HIGH)

sleep(1)

print("Stopping motor")
GPIO.output(Motor3E, GPIO.LOW)


print("Going backwards!")
GPIO.output(Motor3A, GPIO.LOW)
GPIO.output(Motor3B, GPIO.HIGH)
GPIO.output(Motor3E, GPIO.HIGH)

sleep(1)

print("Stopping motor")
GPIO.output(Motor3E, GPIO.LOW)

#Motor4
print("Going forward!")
GPIO.output(Motor4A, GPIO.HIGH)
GPIO.output(Motor4B, GPIO.LOW)
GPIO.output(Motor4E, GPIO.HIGH)

sleep(3)

print("Stopping motor")
GPIO.output(Motor4E, GPIO.LOW)


print("Going backwards!")
GPIO.output(Motor4A, GPIO.LOW)
GPIO.output(Motor4B, GPIO.HIGH)
GPIO.output(Motor4E, GPIO.HIGH)

sleep(3)

print("Stopping motor")
GPIO.output(Motor4E, GPIO.LOW)

GPIO.cleanup()
