from pynput import keyboard


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))


def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        return False


class KeyboardInputService:
    TAG = "KeyboardInputService"

    def __init__(self, logger, power_service):
        self.logger = logger
        self.power_service = power_service
        self.is_listening = False
        self.print_input = False
        self.listener = keyboard.Listener(on_press=on_press, on_release=on_release)
        self.logger.log(self.TAG, "KeyboardInputService instantiated")

    def start_listening(self, print_input=False):
        self.print_input = print_input
        self.is_listening = True

        self.listener.start()
        self.logger.log(self.TAG, "Starting to listen")

    def stop_listening(self):
        self.is_listening = False
        self.logger.log(self.TAG, "Listening stopped")

    def notify_listeners(self, keyboard_input):
        if self.print_input:
            self.logger.log(self.TAG, "Keyboard input : " + keyboard_input, True)

        pass

    def read_input(self):
        return self.stdscr.getkey()
