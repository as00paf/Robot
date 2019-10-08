from logs.LoggingService import LoggingService
from power.BatterySensorService import BatterySensorService
from power.BatterySensorServiceConfiguration import BatterySensorServiceConfiguration
from power.ChargeDetectorService import ChargeDetectorService
from power.ChargeDetectorServiceConfiguration import ChargeDetectorServiceConfiguration
from power.PowerService import PowerService
from flask import Flask
from web import webapp
import os
import time


class RobotMain:
    TAG = "RobotMain"

    logger = None  # type: LoggingService
    battery_service = None  # type: BatterySensorService
    power_service = None  # type: PowerService
    keyboard_service = None  # type: KeyboardInputService
    charge_detector_service = None  # type: ChargeDetectorService

    is_running = False

    def init_services(self):
        # General Services
        self.logger = LoggingService()

        # Power services
        battery_service_config = BatterySensorServiceConfiguration(0, 0, 10, True)
        self.battery_service = BatterySensorService(self.logger, battery_service_config)

        charge_detector_service_config = ChargeDetectorServiceConfiguration(22, 1)
        self.charge_detector_service = ChargeDetectorService(self.logger, charge_detector_service_config)

        self.power_service = PowerService(self.logger, self.battery_service)

        # Input services
        # self.keyboard_service = KeyboardInputService(self.logger, self.power_service)

        # Web services
        self.webapp = Flask(__name__)
        self.webapp.run(host='0.0.0.0', port='8000', debug=True)

        time.sleep(0.5)
        self.logger.log(self.TAG, "All services initialized", True)

    def start_main_loop(self):
        self.is_running = True

        # TODO: move ?
        # self.keyboard_service.start_listening(True)

        while self.is_running:
            pass
        # TODO : move too ?
        # self.keyboard_service.stop_listening()

    def __init__(self):
        try:
            self.init_services()
            self.start_main_loop()

        except KeyboardInterrupt:
            self.stop_running()
            print("You cancelled the operation")
        except Exception as e:
            self.stop_running()
            print("Exception : " + str(e))

    def stop_running(self):
        self.is_running = False
        self.charge_detector_service.stop_monitoring()


@webapp.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    main = RobotMain()
