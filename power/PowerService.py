class PowerService:
    TAG = "PowerService"

    def __init__(self, logger, battery_service):
        self.logger = logger
        self.batteryService = battery_service
        self.logger.log(self.TAG, "PowerService instantiated")