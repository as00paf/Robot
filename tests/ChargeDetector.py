import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()

print("-------------")
print(" Charge Detector ")
print("-------------")

detector_io = 22

GPIO.setup(detector_io, GPIO.IN)

is_charging = False

print("Waiting for you to change the charging state")
while True:
    was_charging = is_charging
    is_charging = GPIO.input(detector_io) == 0

    if was_charging != is_charging:
        print("Charge detected : {0}".format(is_charging))

    time.sleep(1)
