from logs.LoggingService import LoggingService
from input.BluetoothService import BluetoothService

logger = LoggingService()
service = BluetoothService(logger)

service.monitor_gamepad()
