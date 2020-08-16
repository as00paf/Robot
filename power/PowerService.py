from logs.LoggingService import LoggingService
from power.ChargeDetectorService import ChargeDetectorService
from power.BatterySensorService import BatterySensorService
from power.BatteryLevel import BatteryLevel


class PowerService:
    TAG = "PowerService"

    def __init__(self, config, logger):
        self.logger = logger
        self.is_monitoring = False
        self.is_charging = False
        self.battery_level = BatteryLevel.UNDEFINED
        self.battery_percent = 0
        self.charge_service = ChargeDetectorService(config, logger)
        self.battery_service = BatterySensorService(config, logger)

        self.logger.log(self.TAG, "PowerService instantiated")

    def start_monitoring(self):
        self.battery_service.start_monitoring()
        self.battery_service.register_listener(TAG, self)
        
        self.charge_service.register_listener(TAG, self)
        self.is_charging = self.charge_sevice.is_charging
        
    def on_charging_state_changed(self, is_charging):
        self.is_charging = is_charging
        
    def on_battery_level_changed(self, percent):
        self.battery_percent = percent
        self.battery_level = percent_to_level(percent)
        
    def percent_to_level(self, percent):
        if percent in range(0, 20):
            return BatteryLevel.CRITICAL
        elif percent in range(21, 40):
            return BatteryLevel.VERY_LOW
        elif percent in range(41, 60):
            return BatteryLevel.LOW
        elif percent in range(61, 99):
            return BatteryLevel.HEALTHY
        elif percent == 100:
            return BatteryLevel.FULL
        else:
            return BatteryLevel.UNDEFINED
            

