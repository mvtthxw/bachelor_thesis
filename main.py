from class_files import scan_process
from class_files import compare_process

import socket
import sys

class cInit:
    def __init__(self, hostname):
        self.hostname = hostname
        self.IPaddress=""
        self.scan_type=""
        self.port_range=""
        self.save_path=""
        self.config_file="files/config/"+ self.hostname
        self.save_path = "files/tmp_result/"+ self.hostname
        self.ReadConfig()
        self.CheckConfig()
        self.Scan()
        self.Compare()

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
            socket.inet_aton(self.IPaddress)  # sprawdza poprawnosc adresu ip
        except socket.error:
            print("Invalid IP address!")

    def CheckScanType(self):
        scan_types = ["-sS -sU -T4 -A -v", "-T4 -A -v", "-sV -T4 -O -F"]
        try:
            self.scan_type in scan_types
        except:
            print("Wrong scan type")

    def Scan(self):
        print("Scanning process. Please wait!")
        scan_process.cScan(self.IPaddress, self.scan_type, self.port_range, self.save_path)

    def Compare(self):
        print("Compare process")
        compare_process.cCompare(self.hostname)

def main():
    cInit(sys.argv[1])

if __name__ == "__main__":
    main()

