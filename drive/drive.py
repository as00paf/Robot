#!/usr/bin/python
import RPi.GPIO as GPIO
import sys, getopt
from time import sleep


def goForward(Motor1A, Motor1B, Motor1E):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(True)

    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)

    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)
    
    return

def goBackward(Motor1A, Motor1B, Motor1E):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(True)

    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)

    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)
    
    return


def stop(Motor1A, Motor1B, Motor1E):
    GPIO.output(Motor1E, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.LOW)
    return

def drive(sleepTime, direction):
    fl = [5, 6, 13] #front left 
    fr = [19, 12, 26] #front right 
    br = [9, 10, 11] #back left 
    bl = [25, 8, 7] #back right

    Motors = [fr, fl, br, bl]
    front = [fr, fl]
    back = [br, bl]
    left = [fl, bl]
    right = [fr, br]
    
    if direction == "f":
        print("==Going Forward ==")
        for motor in Motors:
            goForward(motor[0], motor[1], motor[2])
    elif direction == "b":
        print("==Going Backward ==")
        for motor in Motors:
            goBackward(motor[0], motor[1], motor[2])
    elif direction == "r":
        print("==Going Right ==")
        for motor in left:
            goBackward(motor[0], motor[1], motor[2])
        #for motor in right:
            #goForward(motor[0], motor[1], motor[2])
    elif direction == "l":
        print("==Going Left ==")
        for motor in left:
            goForward(motor[0], motor[1], motor[2])
        for motor in right:
            goBackward(motor[0], motor[1], motor[2])
    else:
        print("== Wrong Direction ! == (" + direction + ")")
        return
    
    sleep(sleepTime)

    print("== Stopping ==")
    for motor in Motors:
        stop(motor[0], motor[1], motor[2])
        
    return

def main(argv):
    sleepTime = 1
    direction = "f"
    
    if len(sys.argv) > 0:
        try:
            opts, args = getopt.getopt(argv,"hs:d:",["sleep=","direction="])
        except getopt.GetoptError:
            print 'drive.py -s <sleepTime>'
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print 'drive.py -s <sleepTime>'
                sys.exit()
            elif opt in ("-s", "--sleep"):
                sleepTime = float(arg)
            elif opt in ("-d", "--direction"):
                direction = arg
                
    drive(sleepTime, direction)
    GPIO.cleanup()


if __name__ == "__main__":
   main(sys.argv[1:])
