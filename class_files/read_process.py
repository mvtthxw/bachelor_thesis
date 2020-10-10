import ipaddress

class cRead:
    def __init__(self, hostname):
        self.hostname=hostname
        self.config_file="files/config/"+ self.hostname
        self.IPaddress=""
        self.scan_type=""
        self.port_range=""
        self.ReadConfig()
        self.CheckConfig()

    def ReadConfig(self):
        with open(self.config_file, 'r') as file:
            configuration=file.read().splitlines()
            self.IPaddress=configuration[0]
            self.scan_type=configuration[1]
            self.port_range=configuration[2]

    def CheckConfig(self):
        self.CheckIP()
        self.CheckScanType()

    def CheckIP(self):
        try:
            ipaddress.ip_address(self.IPaddress)
        except:
            print("Invalid IP address!")

    def CheckScanType(self):
        scan_types = ["-sS -sU -T4", "-T4 -A -v", "-sV -T4 -O -F"]
        if (self.scan_type in scan_types)==False:
            print("Wrong scan type!")
            exit(1)

