from config.Config import MotorConfig
from time import sleep
import RPi.GPIO as GPIO


class DriveService:
    TAG = "DriveService"

    def __init__(self, config, logger):
        self.config = config  # type: MotorConfig
        self.logger = logger
        self.debug_key_input = False
        self.logger.log(self.TAG, "DriveService instantiated")
        self.init_motors()

    def init_motors(self):
        self.logger.log(self.TAG, "Initializing motors")
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        for motor in self.config.motors:
            self.logger.log(self.TAG, "Initializing " + motor.motor_name)
            motor.init_gpios()

    def forward(self, duration):
        if self.debug_key_input:
            msg = "Forward for " + str(duration) + "s"
            self.logger.log(self.TAG, msg)

        for motor in self.config.motors:
            motor.drive()

        sleep(duration)

        for motor in self.config.motors:
            motor.stop()

    def reverse(self, duration):
        if self.debug_key_input:
            msg = "Backward for " + str(duration) + "s"
            self.logger.log(self.TAG, msg)

        for motor in self.config.motors:
            motor.reverse()

        sleep(duration)

        for motor in self.config.motors:
            motor.stop()

    def turn_right(self, duration):
        if self.debug_key_input:
            msg = "Turning right for " + str(duration) + "s"
            self.logger.log(self.TAG, msg)

        motors = [self.config.motor1, self.config.motor2]
        for motor in motors:
            motor.drive()

        sleep(duration)

        for motor in motors:
            motor.stop()

    def turn_left(self, duration):
        if self.debug_key_input:
            msg = "Turning left for " + str(duration) + "s"
            self.logger.log(self.TAG, msg)

        motors = [self.config.motor3, self.config.motor4]
        for motor in motors:
            motor.drive()

        sleep(duration)

        for motor in motors:
            motor.stop()

    def pivot_right(self, duration):
        if self.debug_key_input:
            msg = "Pivoting right for " + str(duration) + "s"
            self.logger.log(self.TAG, msg)

        front = [self.config.motor1, self.config.motor2]
        for motor in front:
            motor.drive()

        back = [self.config.motor3, self.config.motor4]
        for motor in back:
            motor.reverse()

        sleep(duration)

        for motor in self.config.motors:
            motor.stop()

    def pivot_left(self, duration):
        if self.debug_key_input:
            msg = "Pivoting left for " + str(duration) + "s"
            self.logger.log(self.TAG, msg)

        front = [self.config.motor1, self.config.motor2]
        for motor in front:
            motor.reverse()

        back = [self.config.motor3, self.config.motor4]
        for motor in back:
            motor.drive()

        sleep(duration)

        for motor in self.config.motors:
            motor.stop()



