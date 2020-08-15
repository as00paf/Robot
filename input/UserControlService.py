from drive.DriveService import DriveService
from input.KeyboardInputService import KeyboardInputService


class UserControlService:
    TAG = "UserControlService"

    keyboard_input_service = None  # type:KeyboardInputService
    drive_service = None  # type:DriveService

    def __init__(self, keyboard_input_service, drive_service, logger):
        self.logger = logger
        self.keyboard_input_service = keyboard_input_service
        self.drive_service = drive_service
        self.is_listening = False
        self.listeners = {}
        self.logger.log(self.TAG, "UserControlService instantiated")
        self.init_services()

    def init_services(self):
        self.keyboard_input_service.register_listener(self.TAG, self)
        self.keyboard_input_service.start_listening(True)

    def on_key_pressed(self, key):
        if key == "up":
            self.drive_service.forward(0.3)

    def on_key_up(self, key):
        pass

