class BatterySensorServiceConfiguration:
    CMD_DELTA = 128

    def __init__(self, adc_channel, spi_channel, monitoring_delay=10, print_reply_bytes=False):
        self.adc_channel = adc_channel
        self.spi_channel = spi_channel
        self.monitoring_delay = monitoring_delay
        self.print_reply_bytes = print_reply_bytes
