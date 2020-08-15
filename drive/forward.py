#!/usr/bin/python
import RPi.GPIO as GPIO
import sys, getopt
from time import sleep

def setup(Motor1A, Motor1B, Motor1E):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)

def goForward(Motor1A, Motor1B, Motor1E):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(True)

    print("==Going Forward ==")

    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)

def stop(Motor1A, Motor1B, Motor1E):
    print("== Stopping ==")
    GPIO.output(Motor1E, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.LOW)

def runTest(Motors, sleepTime):
    for motor in Motors:
        setup(motor[0], motor[1], motor[2])
    
    for motor in Motors:
        goForward(motor[0], motor[1], motor[2])

    sleep(sleepTime)

    for motor in Motors:
        stop(motor[0], motor[1], motor[2])
        
    return

def main(argv):

    fl = [17, 27, 22] #front left 
    fr = [26, 19, 13] #front right 
    br = [6, 12, 5] #back left 
    bl = [20, 4, 16] #back right

    Motorz = [fr, fl, br, bl]
    sleepTime = 1
    
    if len(sys.argv) > 0:
        inputfile = ''
        try:
            opts, args = getopt.getopt(argv,"hs:",["sleep="])
        except getopt.GetoptError:
            print 'forward.py -s <sleepTime>'
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print 'forward.py -s <sleepTime>'
                sys.exit()
            elif opt in ("-s", "--sleep"):
                sleepTime = float(arg)
                
    runTest(Motorz, sleepTime)
    GPIO.cleanup()


if __name__ == "__main__":
   main(sys.argv[1:])

           
