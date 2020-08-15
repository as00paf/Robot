class Listenable:

    def __init__(self):
        self.is_listening = False
        self.print_input = True
        self.listeners = {}

    def start_listening(self, print_input=False):
        self.print_input = print_input
        self.is_listening = True

    def stop_listening(self):
        self.is_listening = False

    def register_listener(self, name, listener):
        self.listeners[name] = listener

    def unregister_listener(self, name):
        self.listeners.pop(name)

