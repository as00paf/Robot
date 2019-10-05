class BatterySensorService:
    TAG = "BatterySensorService"

    def __init__(self, logger):
        self.logger = logger
        self.logger.log(self.TAG, "BatterySensorService instantiated")

