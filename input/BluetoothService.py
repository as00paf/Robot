import bluetooth
import sys
from evdev import InputDevice, categorize, ecodes
import evdev
from pynput.keyboard import KeyCode
import threading


class BluetoothService:
    TAG = "BluetoothService"
    
    
    def __init__(self, config, control_service, logger):
        self.logger = logger
        self.config = config
        self.is_monitoring = False
        self.control_service = control_service
        
        if self.config.debug:
            self.logger.log(self.TAG, "BluetoothService instantiated")
            self.logger.log(self.TAG, "This device: " + str(bluetooth.read_local_bdaddr()))
        self.gamepad = InputDevice(self.config.input_device)
        if self.config.debug:
            self.logger.log(self.TAG, "Gamepad: " + str(self.gamepad))
        
        self.thread = threading.Thread(target=self.start_monitoring)
        self.thread.start()
            
    def map_to_keyboard(self, code):
        if code == self.config.yBtn:
            return "left"
        elif code == self.config.bBtn:
            return "down"
        elif code == self.config.aBtn:
            return "right"
        elif code == self.config.xBtn:
            return "up"

        elif code == self.config.start:
            return "start"
        elif code == self.config.select:
            return "select"

        elif code == self.config.lTrig:
            return "q"
        elif code == self.config.rTrig:
            return "e"
            
    
    def monitor_gamepad(self):
        for event in self.gamepad.read_loop():            
            if event.type == ecodes.EV_KEY:
                if(event.value == 1):
                    self.control_service.on_key_pressed(KeyCode.from_char(self.map_to_keyboard(event.code)))
                else:
                    self.control_service.on_key_released(KeyCode.from_char(self.map_to_keyboard(event.code)))
                
                '''
                if event.code == yBtn:
                    print("Y" + " is down" + str(event.value ==1))
                elif event.code == bBtn:
                    print("B" + " is down" + str(event.value ==1))
                elif event.code == aBtn:
                    print("A" + " is down" + str(event.value ==1))
                elif event.code == xBtn:
                    print("X" + " is down" + str(event.value ==1))

                elif event.code == start:
                    print("start" + " is down" + str(event.value ==1))
                elif event.code == select:
                    print("select" + " is down" + str(event.value ==1))

                elif event.code == lTrig:
                    print("left bumper" + " is down" + str(event.value ==1))
                elif event.code == rTrig:
                    print("right bumper" + " is down" + str(event.value ==1))
            '''
            elif event.type == ecodes.EV_ABS:
                if event.code == ecodes.ABS_Y:
                    if event.value < 128:
                        # print("up" + " is down" + str(event.value < 127))
                        if event.value < 127:
                            self.control_service.on_key_pressed(KeyCode.from_char("w"))
                        else:
                            self.control_service.on_key_released(KeyCode.from_char("w"))
                    else:
                        if event.value > 128:
                            self.control_service.on_key_pressed(KeyCode.from_char("s"))
                        else:
                            self.control_service.on_key_released(KeyCode.from_char("s"))
                elif event.code == ecodes.ABS_X:
                    if event.value < 128:
                        if event.value < 127:
                            self.control_service.on_key_pressed(KeyCode.from_char("a"))
                        else:
                            self.control_service.on_key_released(KeyCode.from_char("a"))
                    else:
                        if event.value < 127:
                            self.control_service.on_key_pressed(KeyCode.from_char("d"))
                        else:
                            self.control_service.on_key_released(KeyCode.from_char("d"))
            

            
    
    def find_nearby_devices(self, dur=8):
        nearby_devices = bluetooth.discover_devices(duration=dur, lookup_names=True, flush_cache=False, lookup_class=True)
        self.logger.log(self.TAG, "Found {} devices.".format(len(nearby_devices)))

        devices = []
        for addr, name in nearby_devices:
            self.logger.log(self.TAG, "  {} - {}".format(addr, name))
            devices.append(name)
        
        return devices
                
    
    def get_services_for_device(self, address):
        services = bluetooth.find_service(address=target)

        if len(services) > 0:
            self.logger.log(self.TAG, "Found {} services on {}.".format(len(services), sys.argv[1]))
        else:
            self.logger.log(self.TAG, "No services found.")
            
        for svc in services:
            self.logger.log(self.TAG, "\nService Name:", svc["name"])
            self.logger.log(self.TAG, "    Host:       ", svc["host"])
            self.logger.log(self.TAG, "    Description:", svc["description"])
            self.logger.log(self.TAG, "    Provided By:", svc["provider"])
            self.logger.log(self.TAG, "    Protocol:   ", svc["protocol"])
            self.logger.log(self.TAG, "    channel/PSM:", svc["port"])
            self.logger.log(self.TAG, "    svc classes:", svc["service-classes"])
            self.logger.log(self.TAG, "    profiles:   ", svc["profiles"])
            self.logger.log(self.TAG, "    service id: ", svc["service-id"])
        
        return services
            
            
    def get_local_address(self):
        return str(bluetooth.read_local_bdaddr())

    def start_monitoring(self):
        self.is_monitoring = True
        self.monitor_gamepad()

        if self.config.debug:
            self.logger.log(self.TAG, "Monitoring started")

    def stop_monitoring(self):
        self.is_listening = False
        selg.gamepad.close()
        if self.config.debug:
            self.logger.log(self.TAG, "Monitoring stopped")

    def on_press(self, key):
        try:
            if self.is_listening:
                self.notify_listeners(key, True)
        except Exception as e:
            print("Exception : ", e)
            pass

    def on_release(self, key):
        try:
            if self.is_listening:
                self.notify_listeners(key, False)
        except Exception as e:
            #print("Exception : ", e)
            pass

    def register_listener(self, name, listener):
        self.listeners[name] = listener

    def unregister_listener(self, name):
        self.listeners.pop(name)

    def notify_listeners(self, key, is_pressed):
        for listener in self.listeners.values():
            if is_pressed:
                listener.on_key_pressed(key)
            else:
                listener.on_key_released(key)
                
        if self.print_input:
            if is_pressed:
                self.logger.log(self.TAG, "Bluetooth input : " + '{0} pressed'.format(key), True)
            else:
                self.logger.log(self.TAG, "Bluetooth input : " + '{0} released'.format(key), True)


