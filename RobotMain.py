import time
import traceback
import sys

from flask import Flask
from pynput import keyboard

from config.Config import MotorConfig
from config.Config import PowerConfig
from config.Config import DistanceConfig
from config.Config import UserControlConfig
from config.Config import MenuConfig
from config.Config import KeyboardServiceConfig
from input.UserControlService import UserControlService
from logs.LoggingService import LoggingService
from power.BatterySensorService import BatterySensorService
from power.ChargeDetectorService import ChargeDetectorService
from power.PowerService import PowerService
from input.KeyboardInputService import KeyboardInputService
from file.FileService import FileService
from drive.DriveService import DriveService
from distance.DistanceService import DistanceService
from menu.MenuService import MenuService
from webapp import create_app


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
    menu_service = None  # type: MenuService

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
        keyboard_config = KeyboardServiceConfig()
        self.keyboard_service = KeyboardInputService(keyboard_config, self.logger)
        user_control_config = UserControlConfig()
        self.user_control_service = UserControlService(user_control_config, self.keyboard_service, self.drive_service, self.logger)

        # Power service
        power_config = PowerConfig()
        self.power_service = PowerService(power_config, self.logger)

        # Menu
        menu_config = MenuConfig()
        self.menu_service = MenuService(menu_config, self.keyboard_service, self.power_service, self.logger)

        # Web services
        self.webapp = create_app()
        self.webapp.init(self)

        self.logger.log(self.TAG, "All services initialized")

    def start_main_loop(self):
        self.is_running = True
        
        self.keyboard_service.register_listener(self.TAG, self)
        
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
            pass

    def stop_running(self):
        self.is_running = False
        
        try:
            self.power_service.stop_loops()
            self.distance_service.stop_monitoring()
            self.menu_service.stop_monitoring()
            
            self.user_control_service.stop_loop()
            self.keyboard_service.unregister_listener(self.TAG)
            self.keyboard_service.stop_listening()
        except Exception as e:
            print("Error :" + e)
        finally:
            pass
        
    def on_key_released(self, key):
        pass
        
    def on_key_pressed(self, key):
        if key == keyboard.Key.esc:
            self.logger.log(self.TAG, "You pressed Esc, terminating the Robot's program", True)
            self.stop_running()

if __name__ == "__main__":
    main = RobotMain()
