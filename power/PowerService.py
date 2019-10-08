from logs.LoggingService import LoggingService
from power.BatterySensorService import BatterySensorService


class PowerService:
    TAG = "PowerService"

    def __init__(self, logger, battery_service):
        self.logger = logger
        self.is_monitoring = False
        self.battery_service = battery_service

        self.logger.log(self.TAG, "PowerService instantiated")

        # self.start_monitoring()

    def start_monitoring(self):
        self.battery_service.start_monitoring()

