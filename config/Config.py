from drive.models.Motor import Motor


class MotorConfig:

    def __init__(self):
        motor1_a = 16
        motor1_b = 20
        motor1_e = 21

        motor2_a = 13
        motor2_b = 19
        motor2_e = 26

        motor3_a = 4
        motor3_b = 17
        motor3_e = 6

        motor4_a = 12
        motor4_b = 22
        motor4_e = 27

        self.motor1 = Motor("Front Left")
        self.motor1.setup(motor1_a, motor1_b, motor1_e)
        
        self.motor2 = Motor("Front Right")
        self.motor2.setup(motor2_a, motor2_b, motor2_e)
        
        self.motor3 = Motor("Back Left")
        self.motor3.setup(motor3_a, motor3_b, motor3_e)
        
        self.motor4 = Motor("Back Right")
        self.motor4.setup(motor4_a, motor4_b, motor4_e)
        
        self.motors = [self.motor1, self.motor2, self.motor3, self.motor4]
