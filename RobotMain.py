import time
import traceback

from flask import Flask

from config.Config import MotorConfig
from config.Config import PowerConfig
from config.Config import DistanceConfig
from input.UserControlService import UserControlService
from logs.LoggingService import LoggingService
from power.BatterySensorService import BatterySensorService
from power.ChargeDetectorService import ChargeDetectorService
from power.PowerService import PowerService
from input.KeyboardInputService import KeyboardInputService
from file.FileService import FileService
from drive.DriveService import DriveService
from distance.DistanceService import DistanceService


class RobotMain:
    TAG = "RobotMain"

    logger = None  # type: LoggingService
    file_service = None # type: FileService
    drive_service = None # type: DriveService
    motor_config = None # MotorConfig
    battery_service = None  # type: BatterySensorService
    power_service = None  # type: PowerService
    keyboard_service = None  # type: KeyboardInputService
    user_control_service = None  # type: UserControlService
    charge_detector_service = None  # type: ChargeDetectorService
    distance_service = None  # type: DistanceService

    is_running = False

    def init_services(self):
        # General Services
        self.logger = LoggingService()
        self.file_service = FileService(self.logger)

        # Drive Services
        distance_config = DistanceConfig()
        self.distance_service = DistanceService(distance_config, self.logger)
        # will need distance service eventually
        motor_config = MotorConfig()
        self.drive_service = DriveService(motor_config, self.logger)

        # Input services
        self.keyboard_service = KeyboardInputService(self.logger)
        self.user_control_service = UserControlService(self.keyboard_service, self.drive_service, self.logger)

        # Power service
        power_config = PowerConfig()
        self.power_service = PowerService(power_config, self.logger)

        # Web services
        # self.webapp = Flask(__name__)
        # self.webapp.run(host='0.0.0.0', port='8000', debug=True)

        # time.sleep(0.5)
        self.logger.log(self.TAG, "All services initialized", True)

    def start_main_loop(self):
        self.is_running = True
        
        while(self.is_running):
            pass

    def __init__(self):
        try:
            self.init_services()
            self.start_main_loop()

        except KeyboardInterrupt:
            self.stop_running()
            print("You cancelled the operation")
        except Exception as e:
            self.stop_running()
            print("Exception : ", e)
        finally:
            print(traceback.format_exc())

    def stop_running(self):
        self.is_running = False
        
        self.user_control_service.stop_loop()
        self.keyboard_service.stop_listening()
        self.power_service.stop_loops()
        self.distance_service.stop_monitoring()


if __name__ == "__main__":
    main = RobotMain()
