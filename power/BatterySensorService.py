from __future__ import division

import spidev
import time


class BatterySensorService:
    TAG = "BatterySensorService"

    def __init__(self, config, logger):
        self.logger = logger
        self.config = config
        self.is_monitoring = False
        self.battery_level = self.read_sensor(True)
        self.listeners = {}
        self.logger.log(self.TAG, "BatterySensorService instantiated")

    def start_monitoring(self):
        self.logger.log(self.TAG, "Monitoring started")
        self.is_monitoring = True
        self.monitor()

    def monitor(self):
        while self.is_monitoring:
            new_level = self.read_sensor()
            if self.battery_level != new_level:
                self.logger(self.TAG, "Battery level {0}%".format(new_level), True)
                self.notify_listeners(new_level)
            self.battery_level = new_level
            time.sleep(self.config.monitoring_delay)

    def read_sensor(self, is_first_time=False):
        # Spi
        # TODO : move to spidev service ?
        conn = spidev.SpiDev(0, self.config.spi_channel)
        conn.max_speed_hz = 1200000  # 1.2Mhz
        conn.mode = 0

        # Command
        cmd = self.config.CMD_DELTA

        if self.config.adc_channel:
            cmd += 32

        # Reading
        reply_bytes = conn.xfer2([cmd, 0])
        if self.config.print_reply_bytes and not is_first_time:
            print("reply bytes: ", reply_bytes)

        reply_bitstring = ''.join(self.bitstring(n) for n in reply_bytes)
        reply = reply_bitstring[5:15]

        return int(reply, 2) / 2 ** 10

    def bitstring(self, n):
        s = bin(n)[2:]
        return '0' * (8 - len(s)) + s

    def stop_monitoring(self):
        self.is_monitoring = False
        self.logger.log(self.TAG, "Monitoring stopped")

    def register_listener(self, name, listener):
        self.listeners[name] = listener

    def unregister_listener(self, name):
        self.listeners.pop(name)

    def notify_listeners(self, battery_level):
        for listener in self.listeners:
            listener.on_battery_level_changed(battery_level)
