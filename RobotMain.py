from logs.LoggingService import LoggingService
from power.BatterySensorService import BatterySensorService
from power.BatterySensorServiceConfiguration import BatterySensorServiceConfiguration
from power.ChargeDetectorService import ChargeDetectorService
from power.ChargeDetectorServiceConfiguration import ChargeDetectorServiceConfiguration
from power.PowerService import PowerService
import os
import time

if not os.environ["IS_OVER_SSH"]:
    from input.KeyboardInputService import KeyboardInputService


class RobotMain:
    TAG = "RobotMain"

    logger = None  # type: LoggingService
    battery_service = None  # type: BatterySensorService
    power_service = None  # type: PowerService
    keyboard_service = None  # type: KeyboardInputService

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
        if not os.environ["IS_OVER_SSH"]:
            self.keyboard_service = KeyboardInputService(self.logger, self.power_service)

        time.sleep(0.5)
        self.logger.log(self.TAG, "All services initialized", True)

    def start_main_loop(self):
        self.is_running = True

        # TODO: move ?
        if not os.environ["IS_OVER_SSH"]:
            self.keyboard_service.start_listening(True)

        while self.is_running:
            pass
        # TOOD : move too ?
        self.keyboard_service.stop_listening()

    def __init__(self):
        try:
            self.init_services()
            self.start_main_loop()

        except KeyboardInterrupt:
            self.is_running = False
            print("You cancelled the operation")
        except Exception as e:
            self.is_running = False
            print("Exception : " + str(e))


if __name__ == "__main__":
    main = RobotMain()
