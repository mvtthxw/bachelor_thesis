from class_files import scan_process
from class_files import compare_process

import socket
import sys
import os
import nmap
import datetime

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
        self.CheckStatus()

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
        if (self.scan_type in scan_types)==False:
            print("Wrong scan type!")
            exit(1)

    def CheckStatus(self):
        nm = nmap.PortScanner()
        nm.scan(self.IPaddress)
        if len(nm.all_hosts())==0:
            print('Host is down')
            now = datetime.datetime.now()
            year = now.strftime("%Y")
            month = now.strftime("%m")
            day = now.strftime("%d")
            time = now.strftime("%H:%M:%S")
            self.time_now = ('{}-{}-{} {}').format(day, month, year, time)
            self.report=self.time_now+ '\nHost is down'
            with open('files/report/' + self.hostname, 'a') as file:
                file.write(str(self.report))
        else:
            self.Scan()
            self.Compare()

    def Scan(self):
        print("Scanning process. Please wait!")
        scan_process.cScan(self.IPaddress, self.scan_type, self.port_range, self.save_path)

    def Compare(self):
        print("Compare process")
        compare_process.cCompare(self.hostname)

def main():
    if len(sys.argv)!=2:
        print('Wrong number of arguments! Please enter only the config file in argument!')
        sys.exit(1)
    elif os.path.isfile("files/config/"+sys.argv[1])==False:
        print('Config file does not exist')
        sys.exit(1)
    else:
        cInit(sys.argv[1])

if __name__ == "__main__":
    main()

