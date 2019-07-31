import time
import botbook_mcp3002 as mcp #

def readPotentiometer():
    global potentiometer
    potentiometer = mcp.readAnalog() #

def main():
    while True:
        readPotentiometer()
        print("The potentiometer value is %i" %potentiometer)#
        time.sleep(0.5)

if __name__ == "__main__":
    main()
