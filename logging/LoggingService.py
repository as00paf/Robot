import datetime
import sys


class LoggingService:
    TAG = "LoggingService"

    def __init__(self):
        self.log(self.TAG, "LoggingService instantiated")

    def log(self, tag, text, clear=False):
        if clear:
            self.delete_last_line()

        now = datetime.datetime.now()
        print(str(now) + "-" + tag + "::" + text)

    def delete_last_line(self):
        # cursor up one line
        sys.stdout.write('\x1b[1A')
        # delete last line
        sys.stdout.write('\x1b[2K')

