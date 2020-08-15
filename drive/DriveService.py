from config.Config import MotorConfig
from time import sleep


class DriveService:
    TAG = "DriveService"

    def __init__(self, config, logger):
        self.config = config  # type: MotorConfig
        self.logger = logger
        self.logger.log(self.TAG, "DriveService instantiated")
        self.init_motors()

    def init_motors(self):
        self.logger.log(self.TAG, "Initializing motors")
        for motor in self.config.motors:
            self.logger.log(self.TAG, "Initializing ", motor.name)
            motor.init_gpios()

    def forward(self, duration):
        msg = "Forward for " + duration + "s"
        self.logger.log(self.TAG, msg)

        for motor in self.config.motors:
            motor.drive()

        sleep(duration)

        for motor in self.config.motors:
            motor.stop()

    def reverse(self, duration):
        msg = "Backward for " + duration + "s"
        self.logger.log(self.TAG, msg)

        for motor in self.config.motors:
            motor.reverse()

        sleep(duration)

        for motor in self.config.motors:
            motor.stop()

    def turn_right(self, duration):
        msg = "Turning right for " + duration + "s"
        self.logger.log(self.TAG, msg)

        motors = [self.config.motor1, self.config.motor2]
        for motor in motors:
            motor.drive()

        sleep(duration)

        for motor in motors:
            motor.stop()

    def turn_left(self, duration):
        msg = "Turning left for " + duration + "s"
        self.logger.log(self.TAG, msg)

        motors = [self.config.motor3, self.config.motor4]
        for motor in motors:
            motor.drive()

        sleep(duration)

        for motor in motors:
            motor.stop()

    def pivot_right(self, duration):
        msg = "Pivoting right for " + duration + "s"
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
        msg = "Pivoting left for " + duration + "s"
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



