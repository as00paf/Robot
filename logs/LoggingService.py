import datetime


class LoggingService:
    TAG = "LoggingService"

    def __init__(self):
        self.log(self.TAG, "LoggingService instantiated")

    def log(self, tag, text, clear=False):
        if clear:
            self.clear()

        now = datetime.datetime.now()
        print(now.strftime("%x") + " " + now.strftime("%X") + "-" + tag + "::" + text)

    def clear(self):
        print("\033[K")


