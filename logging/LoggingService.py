import datetime


class LoggingService:
    TAG = "LoggingService"

    def __init__(self):
        self.log(self.TAG, "LoggingService instantiated")

    def log(self, tag, text):
        now = datetime.datetime.now()
        print(str(now) + "-" + tag + "::" + text)
