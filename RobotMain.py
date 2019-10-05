from logging.LoggingService import LoggingService
from input.KeyboardInputService import KeyboardInputService
from power.BatterySensorService import BatterySensorService
from power.PowerService import PowerService


class RobotMain:
    TAG = "RobotMain"

    logger = None  # type: LoggingService
    battery_service = None  # type: BatterySensorService
    power_service = None  # type: PowerService
    keyboard_service = None  # type: KeyboardInputService

    is_running = False

    def init_services(self):
        self.logger = LoggingService()
        self.battery_service = BatterySensorService(self.logger)
        self.power_service = PowerService(self.logger, self.battery_service)
        self.keyboard_service = KeyboardInputService(self.logger, self.power_service)

        self.logger.log(self.TAG, "All services initialized")

    def start_main_loop(self):
        self.is_running = True
        self.keyboard_service.start_listening(True)
        while self.is_running:
            pass

    def __init__(self):
        try:
            self.init_services()
            self.start_main_loop()

        except KeyboardInterrupt:
            self.is_running = False
            print("You cancelled the operation")
        except Exception as e:
            print("Exception : " + str(e))


if __name__ == "__main__":
    main = RobotMain()
