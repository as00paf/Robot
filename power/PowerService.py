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
        self.config = config
        self.battery_level = BatteryLevel.UNDEFINED
        self.battery_percent = 0
        self.charge_service = ChargeDetectorService(config, logger)
        self.battery_service = BatterySensorService(config, logger)
        
        self.start_monitoring()
        if self.config.debug:
            self.logger.log(self.TAG, "PowerService instantiated")

    def start_monitoring(self):
        self.battery_service.start_monitoring()
        self.battery_service.register_listener(self.TAG, self)
        
        self.charge_service.start_monitoring()
        self.charge_service.register_listener(self.TAG, self)
        
    def on_charging_state_changed(self, is_charging):
        self.is_charging = is_charging
        
    def on_battery_level_changed(self, percent):
        self.battery_percent = percent
        self.battery_level = self.percent_to_level(percent)
        
    def percent_to_level(self, percent):
        if percent in range(0, 10):
            return BatteryLevel.CRITICAL
        elif percent in range(11, 20):
            return BatteryLevel.VERY_LOW
        elif percent in range(21, 30):
            return BatteryLevel.LOW
        elif percent in range(31, 94):
            return BatteryLevel.HEALTHY
        elif range(95, 100):
            return BatteryLevel.FULL
        else:
            return BatteryLevel.UNDEFINED

    def level_to_string(self, level):
        if level == BatteryLevel.CRITICAL:
            return "Critical"
        elif level == BatteryLevel.FULL:
            return "Full"
        elif level == BatteryLevel.HEALTHY:
            return "Healthy"
        elif level == BatteryLevel.LOW:
            return "Low"
        elif level == BatteryLevel.VERY_LOW:
            return "Very Low"
        else:
            return "Undefinde"


    def stop_loops(self):
        self.battery_service.stop_monitoring()
        self.battery_service.unregister_listener(self.TAG)
        
        self.charge_service.stop_monitoring()
        self.charge_service.unregister_listener(self.TAG)
        if self.config.debug:
            self.logger.log(self.TAG, "Monitoring stopped")

    def report(self):
        self.logger.log(self.TAG, "=====Battery Info=====")
        self.logger.log(self.TAG, "Charging: " + str(self.is_charging))
        self.logger.log(self.TAG, "Battery Level: " + self.level_to_string(self.battery_level))
        self.logger.log(self.TAG, "Battery Percent: " + str(self.battery_percent) + "%")
        self.logger.log(self.TAG, "=====Battery Info=====")
            

