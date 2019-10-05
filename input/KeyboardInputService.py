class KeyboardInputService:
    TAG = "KeyboardInputService"

    def __init__(self, logger, power_service):
        self.logger = logger
        self.power_service = power_service
        self.is_listening = False
        self.print_input = False
        self.logger.log(self.TAG, "KeyboardInputService instantiated")

    def start_listening(self, print_input=False):
        self.print_input = print_input
        self.is_listening = True
        while self.is_listening:
            self.notify_listeners(self.read_input())

    def notify_listeners(self, keyboard_input):
        pass

    def read_input(self):
        return 0
