from time import sleep
from pynput import keyboard


class MenuService:
    TAG = "MenuService"

    def __init__(self, config, keyboard_service, power_service, distance_service, wifi_service, logger):
        self.config = config
        self.keyboard_service = keyboard_service
        self.power_service = power_service
        self.distance_service = distance_service
        self.wifi_service = wifi_service
        self.logger = logger
        self.is_in_menu = False
        self.is_confirming_entrance = False

        self.start_monitoring()
        if self.config.debug:
            self.logger.log(self.TAG, "MenuService instantiated")

    def start_monitoring(self):
        self.keyboard_service.register_listener(self.TAG, self)

    def stop_monitoring(self):
        self.keyboard_service.unregister_listener(self.TAG)

    def on_key_pressed(self, key):
        if not self.is_in_menu and not self.is_confirming_entrance:
            try:
                if key == keyboard.Key.f1:
                    self.confirm_entrance()
            except Exception as e:
                if self.config.debug:
                    self.logger.log(self.TAG, "Error: " + str(e))
                pass
            finally:
                if self.is_in_menu:
                    self.exit_menu()

    def on_key_released(self, key):
        pass

    def confirm_entrance(self):
        self.is_confirming_entrance = True
        
        confirmation = input("Are you sure you want to enter menu? (y=yes)")
        
        if confirmation.lower()[-1] == "y" or confirmation.lower()[-3] == "yes":
            self.enter_menu()
        else:
            self.exit_menu()
        

    def exit_menu(self):
        self.is_in_menu = False
        self.is_confirming_entrance = False
        self.logger.log(self.TAG, "Exiting menu...")
        self.logger.log(self.TAG, "=====Robot Menu=====")

    def enter_menu(self):
        self.is_in_menu = True
        self.is_confirming_entrance = False

        self.logger.clear()
        self.logger.log(self.TAG, "=====Robot Menu=====")
        self.logger.log(self.TAG, "Select one of there options")
        self.logger.log(self.TAG, "1- Admin")
        self.logger.log(self.TAG, "2- Power")
        self.logger.log(self.TAG, "3- Remote Controls")
        self.logger.log(self.TAG, "4- Sensors")
        self.logger.log(self.TAG, "5- Status Report")
        self.logger.log(self.TAG, "6- Exit")
        confirmation = input("What you got for me?")
        self.logger.log(self.TAG, "You chose: " + str(confirmation))
        
        if len(confirmation) == 0:
            self.exit_menu()
        elif str(confirmation) == "1":
            self.display_admin_info()
            self.exit_menu()
        elif str(confirmation) == "2":
            self.display_power_info()
            self.exit_menu()
        elif str(confirmation) == "3":
            self.display_remote_controls_info()
            self.exit_menu()
        elif str(confirmation) == "4":
            self.display_sensors_info()
            self.exit_menu()
        elif str(confirmation) == "5":
            self.display_status_report()
            self.exit_menu()
        else:
            self.exit_menu()

    def display_admin_info(self):
        self.logger.log(self.TAG, "Admin Info")
        sleep(1)
        self.exit_menu()
    
    def display_power_info(self):
        self.power_service.report()
        sleep(5)
        self.exit_menu()

    def display_remote_controls_info(self):
        self.logger.log(self.TAG, "Remote Controls Info")
        self.wifi_service.report()
        sleep(1)
        self.exit_menu()

    def display_sensors_info(self):
        self.logger.log(self.TAG, "Sensors Info")
        sleep(1)
        self.exit_menu()

    def display_status_report(self):
        self.logger.log(self.TAG, "Status Report")
        self.power_service.report()
        self.distance_service.report()
        self.wifi_service.report()
        sleep(1)
        self.exit_menu()

