class MenuService:
    TAG = "MenuService"

    def __init__(self, config, keyboard_service, battery_service, logger):
        self.config = config
        self.keyboard_service = keyboard_service
        self.battery_service = battery_service
        self.logger = logger
        self.is_in_menu = False

        self.init_services()

    def init_services(self):
        self.keyboard_service.register_listener(self.TAG, self)

    def on_key_pressed(self, key):
        try:
            if not self.is_in_menu:
                if key.char.lower() == "m":
                    self.confirm_entrance()
        finally:
            pass

    def on_key_released(self):
        pass

    def confirm_entrance(self):
        confirmation = input("Are you sure you want to enter menu? (y=yes) ").lower()
        if confirmation == "y":
            self.enter_menu()
        else:
            self.logger.log(self.TAG, "Operation cancelled")

    def exit_menu(self):
        self.is_in_menu = False
        self.logger.log(self.TAG, "Exiting menu...")
        self.logger.log(self.TAG, "=====Robot Menu=====")

    def enter_menu(self):
        self.is_in_menu = True

        self.logger.clear()
        self.logger.log(self.TAG, "=====Robot Menu=====")
        self.logger.log(self.TAG, "Select one of there options")
        self.logger.log(self.TAG, "1- Battery Info")
        self.logger.log(self.TAG, "2- Exit")
        confirmation = input("What you got for me?")

        if str(confirmation) == "1":
            self.display_battery_info()
        else:
            self.exit_menu()

    def display_battery_info(self):
        self.battery_service.report()
        self.enter_menu()

