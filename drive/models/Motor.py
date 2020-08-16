import RPi.GPIO as GPIO


class Motor:

    def __init__(self, motor_name):
        self.motor_name = motor_name
        
    def setup(self, ma, mb, me):
        self.ma = ma
        self.mb = mb
        self.me = me

    def init_gpios(self):
        GPIO.setup(self.ma, GPIO.OUT)
        GPIO.setup(self.mb, GPIO.OUT)
        GPIO.setup(self.me, GPIO.OUT)

    def reverse(self):
        GPIO.output(self.ma, GPIO.LOW)
        GPIO.output(self.mb, GPIO.HIGH)
        GPIO.output(self.me, GPIO.HIGH)

    def drive(self):
        GPIO.output(self.ma, GPIO.HIGH)
        GPIO.output(self.mb, GPIO.LOW)
        GPIO.output(self.me, GPIO.HIGH)

    def stop(self):
        GPIO.output(self.me, GPIO.LOW)
