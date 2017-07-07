#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

print("-------------")
print(" HelloBot ")
print("-------------")


def runTest(Motor1A, Motor1B, Motor1E):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(True)

    print("==Starting test==")

    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)

    print("Turning motor on!")
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)

    sleep(3)

    print("Stopping motor")
    GPIO.output(Motor1E, GPIO.LOW)
    
    sleep(1)

    print("Going backwards!")
    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

    sleep(3)

    print("==Test Complete==")
    GPIO.output(Motor1E, GPIO.LOW)

    GPIO.cleanup()

    return

#runTest(5, 6, 13) #front left 
#runTest(19, 12, 26) #front right

runTest(19, 26, 12) #front but no back
#runTest(12, 19, 26) #no front but back
#runTest(26, 19, 12) no front but back

#runTest(9, 10, 11) #back left 
#runTest(25, 8, 7) #back right 
            
