#!/usr/bin/python
import RPi.GPIO as GPIO
import sys, getopt
from time import sleep


def goBackward(Motor1A, Motor1B, Motor1E):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(True)

    print("==Going Backward ==")

    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)

    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)
    
    return

def stop(Motor1A, Motor1B, Motor1E):
    print("== Stopping ==")
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.LOW)
    return

def runTest(Motors, sleepTime):
    for motor in Motors:
        goBackward(motor[0], motor[1], motor[2])

    sleep(sleepTime)

    for motor in Motors:
        stop(motor[0], motor[1], motor[2])


def main(argv):
    fl = [5, 6, 13] #front left
    fr = [19, 12, 26] #front right
    br = [9, 10, 11] #back left
    bl = [25, 8, 7] #back right

    Motorz = [fr, fl, bl, br]
    sleepTime = 1

    if len(sys.argv) > 0:
        inputfile = ''
        try:
            opts, args = getopt.getopt(argv,"hs:",["sleep="])
        except getopt.GetoptError:
            print 'backward.py -s <sleepTime>'
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print 'backward.py -s <sleepTime>'
                sys.exit()
            elif opt in ("-s", "--sleep"):
                sleepTime = float(arg)
    runTest(Motorz, sleepTime)
    GPIO.cleanup()

if __name__ == "__main__":
    main(sys.argv[1:])
           
