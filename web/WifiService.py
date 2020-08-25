import socket
import subprocess
from wifi import Cell, Scheme
from logs.LoggingService import LoggingService

class WifiService:
    TAG = "WifiService"
    
    def __init__(self, config, logger):
        self.logger = logger
        self.config = config
        self.is_monitoring = False
        self.is_on = self.is_wifi_on()
        self.is_connected = self.is_wifi_connected()
        self.ssid = self.get_ssid()   
        if self.config.debug:
            self.logger.log(self.TAG, "WifiService instantiated")     
        
        if self.config.monitor:
            self.start_monitoring()
        
    def is_wifi_on(self):
        return len(list(Cell.all('wlan0'))) != 0

    def is_wifi_connected(self):
        try:
            socket.create_connection(("1.1.1.1", 53))
            return True
        except Exception:
            pass
        return False
        
    def get_ssid(self):
        ssid = None
        ps = subprocess.Popen(['iwgetid'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        try:
            output = subprocess.check_output(('grep', 'ESSID'), stdin=ps.stdout)
            ssid = str(output).split('"', 1)[1].split('"', 1)[0]
        except subprocess.CalledProcessError:
            # grep did not match any lines
            ssid = "No wireless networks connected"
        return ssid
        
        
    def get_available_ssids(self):
        self.ssids =  Cell.all('wlan0')
        return self.ssids
        
    def get_available_ssids_str(self):
        self.get_available_ssids()
        result = ""
        for ssid in self.ssids:
            result = result + str(ssid) + '\n'
        return result
        
        
    def find_ssid_by_name(self, name):
        wifilist = self.get_available_ssids()
        
        for cell in wifilist:
            if cell.ssid == name:
                return cell
        
        return False
        
    def find_from_saved_list(self, name):
        cell = wifi.Scheme.find('wlan0', name)

        if cell:
            return cell

        return False
        
        
    def save(self, cell, password):
        if not cell:
            return False

        scheme = wifi.Scheme.for_cell('wlan0', cell.ssid, cell, password)
        scheme.save()
        return scheme


    def delete(self, ssid):
        if not ssid:
            return False

        cell = self.find_from_saved_list(ssid)

        if cell:
            cell.delete()
            return True

        return False
        
        
    def Connect(ssid, password=None):
        cell = get_available_ssids(ssid)

        if cell:
            savedcell = FindFromSavedList(cell.ssid)

            # Already Saved from Setting
            if savedcell:
                savedcell.activate()
                return cell

            # First time to connect
            else:
                if cell.encrypted:
                    if password:
                        scheme = Add(cell, password)

                        try:
                            scheme.activate()

                        # Wrong Password
                        except wifi.exceptions.ConnectionError:
                            # Delete(ssid)
                            return False

                        return cell
                    else:
                        return False
                else:
                    scheme = Add(cell)

                    try:
                        scheme.activate()
                    except wifi.exceptions.ConnectionError:
                        Delete(ssid)
                        return False

                    return cell
        
        return False
        
        
    def start_monitoring(self):
        if self.config.debug:
            self.logger.log(self.TAG, "Monitoring started")
        self.is_monitoring = True
        self.thread = threading.Thread(target=self.monitor)
        self.thread.start()
        
    def monitor(self):
        while self.is_monitoring:
            self.measure_all()
            sleep(self.config.monitoring_delay)
            
    def stop_monitoring(self):
        self.is_monitoring = False
        if self.config.debug:
            self.logger.log(self.TAG, "Monitoring stopped")
        
    def report(self):
        self.logger.log(self.TAG, "=====Wifi Info=====")
        self.logger.log(self.TAG, "Monitoring: " + str(self.is_monitoring))
        self.logger.log(self.TAG, "Wifi On: " + str(self.is_wifi_on()))
        self.logger.log(self.TAG, "Wifi Connected: " + str(self.is_wifi_connected()))
        self.logger.log(self.TAG, "SSID: " + str(self.get_ssid()))
        self.logger.log(self.TAG, "Available SSIDs: " + str(self.get_available_ssids_str()))
        self.logger.log(self.TAG, "=====Wifi Info=====")
        
    #todo: add menu here
