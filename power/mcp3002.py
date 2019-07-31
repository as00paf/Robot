import RPi.GPIO as GPIO
import sys
import time

class MCP3002:
    def setup(self, CLK=11, MOSI=10, MISO=11, CS=8):
        #setup
        
        self.CLK = CLK
        self.MOSI = MOSI
        self.MISO = MISO
        self.CS = CS

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        print "CLK %d" %(self.CLK)
        GPIO.setup(self.CLK, GPIO.OUT)
        GPIO.setup(self.MOSI, GPIO.OUT)
        GPIO.setup(self.MISO, GPIO.IN)
        GPIO.setup(self.CS, GPIO.OUT)
        print "Setup complete"

    def cleanup(self):
        GPIO.cleanup()

    def read_sensor(self, channel=0):
        self.setup()
        if(channel == 0):
            cmd = 0x6
        else:
            cmd = 0x7

        #init pins low
        GPIO.setup(self.CLK, GPIO.OUT)
        GPIO.output(self.CLK, False)
        GPIO.output(self.CS, False)

        #write first 3 bits to MOSI
        cmd <<= 5
        for bno in range(3):
            if(cmd & 0x80):
                GPIO.output(self.MOSI, True)
            else:
                GPIO.output(self.MOSI, False)

            cmd <<= 1
            GPIO.output(self.CLK, True)
            GPIO.output(self.CLK, False)

        # read 2(empty and null bit) + 10 ADC bits from MISO
        adc_result = 0
        for bit_no in range(12):
            GPIO.output(self.CLK, True)
            GPIO.output(self.CLK, False)
            adc_result <<= 1
            if(GPIO.input(self.MISO)):
                adc_result |= 0x1

        GPIO.output(self.CLK, True)

        adc_result /= 2 #first bit is null so drop it
        return adc_result

if __name__ == "__main__":
    print "Setting up"
    mcp =  MCP3002()

    result = mcp.read_sensor(0)
    print 'result: %d' % (result)
    mcp.cleanup()
