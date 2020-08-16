import RPi.GPIO as GPIO
import time
import threading
from time import sleep


class DistanceService():
    TAG = "DistanceService"
    
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.PIN_TRIGGER = config.trigger_io
        self.PIN_ECHO_F = config.front_io
        self.PIN_ECHO_B = config.back_io
        self.is_monitoring = False
        self.debug = config.debug
        self.distance_front = 0
        self.distance_back = 0
        self.init_gpios()
        self.logger.log(self.TAG, "DistanceService instantiated")
        self.start_monitoring()
        
    def init_gpios(self):
        #TODO : move
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        
        GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(self.PIN_ECHO_F, GPIO.IN)
        GPIO.setup(self.PIN_ECHO_B, GPIO.IN)
        
    def start_monitoring(self):
        self.logger.log(self.TAG, "Monitoring started")
        self.is_monitoring = True
        self.thread = threading.Thread(target=self.monitor)
        self.thread.start()
        
    def monitor(self):
        while self.is_monitoring:
            self.measure_all()
            sleep(self.config.monitoring_delay)
            
    def stop_monitoring(self):
        self.is_monitoring = False
        
    def measure_all(self):
        try:
            self.measure_front()
            self.measure_back()
        except Exception as e:
            print("Exception : ", e)
        
    def measure_back(self):
        try:
            GPIO.output(self.PIN_TRIGGER, GPIO.LOW)
            time.sleep(self.config.sleep_delay)
            GPIO.output(self.PIN_TRIGGER, GPIO.HIGH)
            
            time.sleep(0.00001)
            
            GPIO.output(self.PIN_TRIGGER, GPIO.LOW)
            
            while GPIO.input(self.PIN_ECHO_B)==0:
                pulse_start_time_b = time.time()
            while GPIO.input(self.PIN_ECHO_B)==1:
                pulse_end_time_b = time.time()
            
            pulse_duration_b = pulse_end_time_b - pulse_start_time_b
            distance_b = round(pulse_duration_b * 17150, 2)
            self.distance_back = distance_b
            
            if self.config.debug:
                self.logger.log(self.TAG, "Back distance:" + str(distance_b) + "cm")

        finally:
            pass
    
    def measure_front(self):
        try:
            GPIO.output(self.PIN_TRIGGER, GPIO.LOW)
            time.sleep(self.config.sleep_delay)
            GPIO.output(self.PIN_TRIGGER, GPIO.HIGH)
            
            time.sleep(0.00001)
            
            GPIO.output(self.PIN_TRIGGER, GPIO.LOW)
            
            while GPIO.input(self.PIN_ECHO_F)==0:
                pulse_start_time_f = time.time()
            while GPIO.input(self.PIN_ECHO_F)==1:
                pulse_end_time_f = time.time()
                
            GPIO.output(self.PIN_TRIGGER, GPIO.LOW)
            pulse_duration_f = pulse_end_time_f - pulse_start_time_f
            distance_f = round(pulse_duration_f * 17150, 2)
            self.distance_front = distance_f
            if self.config.debug:
                self.logger.log(self.TAG, "Front distance:" + str(distance_f) + "cm")
            
        finally:
            pass

