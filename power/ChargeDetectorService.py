import time
import RPi.GPIO as GPIO
from threading import Thread


class ChargeDetectorService:
    TAG = "ChargeDetectorService"

    def __init__(self, logger, configuration):
        self.logger = logger
        self.configuration = configuration
        self.is_charging = False
        self.is_monitoring = False
        self.thread = Thread(target=self.monitor)
        self.listeners = {}
        self.logger.log(self.TAG, "ChargeDetectorService instantiated")
        self.init_gpio()
        self.start_monitoring()

    # TODO : move to gpio service ?
    def init_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setup(self.configuration.detector_io, GPIO.IN)

    def start_monitoring(self):
        self.logger.log(self.TAG, "Monitoring started")
        self.is_monitoring = True
        self.thread.start()

    def monitor(self):
        while self.is_monitoring:
            was_charging = self.is_charging
            self.is_charging = self.read_charging_state()

            if was_charging != self.is_charging:
                self.logger.log(self.TAG, "Charge detected : {0}".format(self.is_charging), True)
                self.notify_listeners(self.is_charging)

            time.sleep(self.configuration.monitor_sleep_time)

    def stop_monitoring(self):
        self.is_monitoring = False
        self.logger.log(self.TAG, "Monitoring stopped")

    def read_charging_state(self):
        return GPIO.input(self.configuration.detector_io) != 0

    def register_listener(self, name, listener):
        self.listeners[name] = listener

    def unregister_listener(self, name):
        self.listeners.pop(name)

    def notify_listeners(self, is_charging):
        for key in self.listeners:
            self.listeners[key].on_charging_state_changed(is_charging)

