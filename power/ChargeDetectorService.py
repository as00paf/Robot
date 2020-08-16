import time
import RPi.GPIO as GPIO
import threading


class ChargeDetectorService:
    TAG = "ChargeDetectorService"

    def __init__(self, config, logger):
        self.logger = logger
        self.config = config
        self.is_charging = False
        self.is_monitoring = False
        self.listeners = {}
        self.logger.log(self.TAG, "ChargeDetectorService instantiated")
        self.init_gpio()

    def init_gpio(self):
        GPIO.setup(self.config.detector_io, GPIO.IN)

    def start_monitoring(self):
        self.logger.log(self.TAG, "Monitoring started")
        self.is_monitoring = True
        self.thread = threading.Thread(target=self.monitor)
        self.thread.start()

    def monitor(self):
        while self.is_monitoring:
            was_charging = self.is_charging
            self.is_charging = self.read_charging_state()

            if was_charging != self.is_charging:
                if self.config.debug:
                    self.logger.log(self.TAG, "Charge detected : {0}".format(self.is_charging), True)
                self.notify_listeners(self.is_charging)

            time.sleep(self.config.monitor_sleep_time)

    def stop_monitoring(self):
        self.is_monitoring = False
        self.logger.log(self.TAG, "Monitoring stopped")

    def read_charging_state(self):
        return GPIO.input(self.config.detector_io) != 0

    def register_listener(self, name, listener):
        self.listeners[name] = listener

    def unregister_listener(self, name):
        self.listeners.pop(name)

    def notify_listeners(self, is_charging):
        for listener in self.listeners.values():
            listener.on_charging_state_changed(is_charging)

