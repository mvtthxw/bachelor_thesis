from class_files import input_data_process
from class_files import scan_process

import nmap
import os


class cFirstScanner:
    def __init__(self):
        self.hostname = ""
        self.IPaddress = ""
        self.scan_type = ""
        self.port_range = "1-65535"
        self.scan_result = ""
        self.Input()
        self.config_path = "files/config/" + self.hostname
        self.def_ports_path = "files/default_ports/" + self.hostname

    def Input(self):
        host = input_data_process.cInput()
        self.hostname = host.hostname
        self.IPaddress = host.IPaddress
        self.scan_type = host.scan_type
        self.port_range = host.port_range

    def CheckStatus(self):
        nm = nmap.PortScanner()
        nm.scan(self.IPaddress)
        if len(nm.all_hosts()) == 0:
            print("Host is down")
        else:
            self.Scan()
            self.SavePorts()
            self.SaveConfig()
            os.system("touch files/report/" + self.hostname)

    def Scan(self):
        oScan = scan_process.cScan(self.IPaddress, self.scan_type, self.port_range)
        self.scan_result = oScan.scan_result

    def SavePorts(self):
        with open(self.def_ports_path, "w+") as file:
            file.write(str(self.scan_result))

    def SaveConfig(self):
        config = self.IPaddress + "\n" + self.scan_type + "\n" + self.port_range
        with open(self.config_path, "w+") as file:
            file.write(str(config))
