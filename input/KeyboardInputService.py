from pynput import keyboard


class KeyboardInputService:
    TAG = "KeyboardInputService"

    def __init__(self, config, logger):
        self.logger = logger
        self.config = config
        self.is_listening = False
        self.print_input = True
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listeners = {}
        if self.config.debug:
            self.logger.log(self.TAG, "KeyboardInputService instantiated")

    def start_listening(self, print_input=False):
        self.print_input = print_input
        self.is_listening = True
        self.listener.start()

        if self.config.debug:
            self.logger.log(self.TAG, "Monitoring started")

    def stop_listening(self):
        self.is_listening = False
        self.listener.stop()
        if self.config.debug:
            self.logger.log(self.TAG, "Monitoring stopped")

    def on_press(self, key):
        try:
            if self.is_listening:
                self.notify_listeners(key, True)
        except Exception as e:
            print("Exception : ", e)
            pass

    def on_release(self, key):
        try:
            if self.is_listening:
                self.notify_listeners(key, False)
        except Exception as e:
            #print("Exception : ", e)
            pass

    def register_listener(self, name, listener):
        self.listeners[name] = listener

    def unregister_listener(self, name):
        self.listeners.pop(name)

    def notify_listeners(self, key, is_pressed):
        for listener in self.listeners.values():
            if is_pressed:
                listener.on_key_pressed(key)
            else:
                listener.on_key_released(key)
                
        if self.print_input:
            if is_pressed:
                self.logger.log(self.TAG, "Keyboard input : " + 'Key {0} pressed'.format(key), True)
            else:
                self.logger.log(self.TAG, "Keyboard input : " + 'Key {0} released'.format(key), True)


