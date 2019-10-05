from logging.LoggingService import LoggingService
from power.BatterySensorService import BatterySensorService


class PowerService:
    TAG = "PowerService"

    def __init__(self, logger, battery_service):
        # type: (LoggingService, BatterySensorService) -> PowerService
        self.logger = logger
        self.batteryService = battery_service
        self.logger.log(self.TAG, "PowerService instantiated")