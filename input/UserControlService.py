from drive.DriveService import DriveService
from input.KeyboardInputService import KeyboardInputService
import threading
from pynput import keyboard


class UserControlService:
    TAG = "UserControlService"

    keyboard_input_service = None  # type:KeyboardInputService
    drive_service = None  # type:DriveService

    def __init__(self, config, keyboard_input_service, drive_service, logger):
        self.config = config
        self.logger = logger
        self.keyboard_input_service = keyboard_input_service
        self.drive_service = drive_service
        self.is_listening = False
        self.listeners = {}
        self.init_services()
        self.thread = threading.Thread(target=self.start_loop)
        self.thread.start()
        if self.config.debug:
            self.logger.log(self.TAG, "UserControlService instantiated")

    def init_services(self):
        self.keyboard_input_service.register_listener(self.TAG, self)
        self.debug_key_input = self.config.debug_key_input
        self.keyboard_input_service.start_listening(self.debug_key_input)

    def on_key_pressed(self, key):
        try:
            if self.debug_key_input:
                self.logger.log(self.TAG, "Key pressed : " + str(key))
            
            if key.char == "up":
                self.up = True
            elif key.char.lower() == "w":
                self.up = True
        
            if key.char == "down":
                self.down = True
            elif key.char.lower() == "s":
                self.down = True
        
            if key.char == "left":
                self.left = True
            elif key.char.lower() == "d":
                self.left = True
        
            if key.char == "right":
                self.right = True
            elif key.char.lower() == "a":
                self.right = True
                
            if key.char.lower() == "e":
                self.pivot_left = True
        
            if key.char.lower() == "q":
                self.pivot_right = True
        
        except AttributeError:
            if self.debug_key_input:
                self.logger.log(self.TAG, "Special key pressed")

    def on_key_released(self, key):
        try:
            if self.debug_key_input:
                self.logger.log(self.TAG, "Key released : " + key.char)
        
            if key.char == "up":
                self.up = False
            elif key.char.lower() == "w":
                self.up = False
        
            if key.char == "down":
                self.down = False
            elif key.char.lower() == "s":
                self.down = False
        
            if key.char == "left":
                self.left = False
            elif key.char.lower() == "d":
                self.left = False
        
            if key.char == "right":
                self.right = False
            elif key.char.lower() == "a":
                self.right = False
        
            if key.char.lower() == "e":
                self.pivot_left = False
        
            if key.char.lower() == "q":
                self.pivot_right = False
        
        except AttributeError:
            if self.debug_key_input:
                self.logger.log(self.TAG, "Special key released")
    
    def start_loop(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.pivot_left = False
        self.pivot_right = False
        self.is_running = True
        
        delay = self.config.drive_delay
        
        while self.is_running:
            if(self.up):
                self.drive_service.forward(delay)
            elif(self.down):
                self.drive_service.reverse(delay)
            elif(self.left):
                self.drive_service.turn_left(delay)
            elif(self.right):
                self.drive_service.turn_right(delay)
            elif(self.pivot_left):
                self.drive_service.pivot_left(delay)
            elif(self.pivot_right):
                self.drive_service.pivot_right(delay)
                
    def stop_loop(self):
        self.is_running = False
        if self.config.debug:
            self.logger.log(self.TAG, "Monitoring stopped")

                

