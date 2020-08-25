from drive.models.Motor import Motor


class MenuConfig:

    def __init__(self):
        self.debug = False


class KeyboardServiceConfig:

    def __init__(self):
        self.debug = False


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

        motor4_a = 22
        motor4_b = 12
        motor4_e = 27
        
        self.debug = False

        self.motor1 = Motor("Front Left")
        self.motor1.setup(motor1_a, motor1_b, motor1_e)
        
        self.motor2 = Motor("Front Right")
        self.motor2.setup(motor2_a, motor2_b, motor2_e)
        
        self.motor3 = Motor("Back Left")
        self.motor3.setup(motor3_a, motor3_b, motor3_e)
        
        self.motor4 = Motor("Back Right")
        self.motor4.setup(motor4_a, motor4_b, motor4_e)
        
        self.motors = [self.motor1, self.motor2, self.motor3, self.motor4]
        

class PowerConfig():
    
    CMD_DELTA = 128  #Or 128 ?
    CLK = 11
    MISO = 9
    MOSI = 10
    
    def __init__(self):
        self.detector_io = 5
        
        self.adc_channel = 0  #Always 0
        self.spi_channel = 0  #GPIO 08
        self.monitoring_delay = 10
        self.print_reply_bytes = False
        
        self.monitor_sleep_time = 1
        self.debug = False
        
        
class DistanceConfig():
    
    def __init__(self):
        self.trigger_io = 18
        self.front_io = 23
        self.back_io = 24
        self.debug = False
        self.monitoring_delay = 2
        self.sleep_delay = 10
        
            
class UserControlConfig():
    
    def __init__(self):
        self.debug = False
        self.debug_key_input = False
        self.drive_delay = 0.05
        

class WebServerConfig():
    
    def __init__(self):
        self.debug = False
        self.host = "0.0.0.0"
        self.drive_delay = 0.05
        

class WifiServiceConfig():
    
    def __init__(self):
        self.debug = False
        self.monitor = False


            
        
        
    

