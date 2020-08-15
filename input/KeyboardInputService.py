from pynput import keyboard


class KeyboardInputService:
    TAG = "KeyboardInputService"

    def __init__(self, logger):
        self.logger = logger
        self.is_listening = False
        self.print_input = True
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listeners = {}
        self.logger.log(self.TAG, "KeyboardInputService instantiated")

    def start_listening(self, print_input=False):
        self.print_input = print_input
        self.is_listening = True
        self.listener.start()

        self.logger.log(self.TAG, "Starting to listen")

    def stop_listening(self):
        self.is_listening = False
        self.listener.stop()
        self.logger.log(self.TAG, "Listening stopped")

    def on_press(self, key):
        if self.is_listening:
            self.notify_listeners(key, True)

    def on_release(self, key):
        if self.is_listening:
            self.notify_listeners(key, False)

    def register_listener(self, name, listener):
        self.listeners[name] = listener

    def unregister_listener(self, name):
        self.listeners.pop(name)

    def notify_listeners(self, key, is_pressed):
        for key in self.listeners:
            if is_pressed:
                self.listeners[key].on_key_pressed(key)
            else:
                self.listeners[key].on_key_released(key)

        if self.print_input:
            if is_pressed:
                self.logger.log(self.TAG, "Keyboard input : " + 'Key {0} pressed'.format(key.name), True)
            else:
                self.logger.log(self.TAG, "Keyboard input : " + 'Key {0} released'.format(key.name), True)
