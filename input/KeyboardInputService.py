import os
import curses

class KeyboardInputService:
    stdscr = None  # type: Object
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
        
        self.stdscr = curses.initscr()
        curses.noecho()
        self.stdscr.keypad(True)
        
        self.logger.log(self.TAG, "Starting to listen")
        while self.is_listening:
            self.notify_listeners(self.read_input())
        self.logger.log(self.TAG, "Listening stopped")

    def stop_listening(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

        self.is_listening = False

    def notify_listeners(self, keyboard_input):
        self.logger.log(self.TAG, "Keyboard input : " + keyboard_input)
        pass

    def read_input(self):
        return self.stdscr.getkey()
