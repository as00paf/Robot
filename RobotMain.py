import time

from flask import Flask

from config.Config import MotorConfig
from logs.LoggingService import LoggingService
from power.BatterySensorService import BatterySensorService
from power.BatterySensorServiceConfiguration import BatterySensorServiceConfiguration
from power.ChargeDetectorService import ChargeDetectorService
from power.ChargeDetectorServiceConfiguration import ChargeDetectorServiceConfiguration
from power.PowerService import PowerService
from file.FileService import FileService
from drive.DriveService import DriveService


class RobotMain:
    TAG = "RobotMain"

    logger = None  # type: LoggingService
    file_service = None # type: FileService
    drive_service = None # type: DriveService
    motor_config = MotorConfig()
    battery_service = None  # type: BatterySensorService
    power_service = None  # type: PowerService
    keyboard_service = None  # type: KeyboardInputService
    charge_detector_service = None  # type: ChargeDetectorService

    is_running = False

    def init_services(self):
        # General Services
        self.logger = LoggingService()
        self.file_service = FileService(self.logger)

        # Drive Services
        # will need distance service eventually
        self.drive_service = DriveService(self.motor_config, self.logger)

        # Power services
        # battery_service_config = BatterySensorServiceConfiguration(0, 0, 10, True)
        # self.battery_service = BatterySensorService(self.logger, battery_service_config)

        # charge_detector_service_config = ChargeDetectorServiceConfiguration(22, 1)
        # self.charge_detector_service = ChargeDetectorService(self.logger, charge_detector_service_config)

        # self.power_service = PowerService(self.logger, self.battery_service)

        # Input services
        # self.keyboard_service = KeyboardInputService(self.logger, self.power_service)

        # Web services
        # self.webapp = Flask(__name__)
        # self.webapp.run(host='0.0.0.0', port='8000', debug=True)

        # time.sleep(0.5)
        self.logger.log(self.TAG, "All services initialized", True)

    def start_main_loop(self):
        self.is_running = True
        '''
        # TODO: move ?
        # self.keyboard_service.start_listening(True)

        while self.is_running:
            pass
        # TODO : move too ?
        # self.keyboard_service.stop_listening()
        '''

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


if __name__ == "__main__":
    main = RobotMain()
