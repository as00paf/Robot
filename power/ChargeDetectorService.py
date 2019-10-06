import time
import RPi.GPIO as GPIO


class ChargeDetectorService:
    TAG = "ChargeDetectorService"

    def __init__(self, logger, configuration):
        self.logger = logger
        self.configuration = configuration
        self.is_charging = False
        self.listeners = {}
        self.logger.log(self.TAG, "ChargeDetectorService instantiated")
        self.init_gpio()

    # TODO : move to gpio service ?
    def init_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.cleanup()
        GPIO.setup(self.configuration.detector_io, GPIO.IN)

    def monitor_charging_state(self):
        while True:
            was_charging = self.is_charging
            self.is_charging = self.read_charging_state()

            if was_charging != self.is_charging:
                self.logger.log(self.TAG, "Charge detected : {0}".format(self.is_charging), True)
                self.notify_listeners(self.is_charging)

            time.sleep(self.configuration.monitor_sleep_time)

    def read_charging_state(self):
        return GPIO.input(self.configuration.detector_io) != 0

    def register_listener(self, name, listener):
        self.listeners[name] = listener

    def unregister_listener(self, name):
        self.listeners.pop(name)

    def notify_listeners(self, is_charging):
        for key in self.listeners:
            self.listeners[key].on_charging_state_changed(is_charging)

