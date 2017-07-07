
#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import os
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

print("-------------")
print(" Button + GPIO ")
print("-------------")


lightIO = 17

GPIO.setup(18, GPIO.IN)
GPIO.setup(lightIO, GPIO.OUT)

lightOn = False

print("Waiting for you to press a button")
while True:
    if(GPIO.input(18) == False):
        print("Button pressed")
        GPIO.output(lightIO, GPIO.HIGH)

        #time.sleep(1)
    else:
            GPIO.output(lightIO, GPIO.LOW)
        
            
