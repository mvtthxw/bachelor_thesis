from class_files import scan_process
from class_files import compare_process

import socket
import os
class cInit:
    def __init__(self):
        self.IPaddress="127.0.0.1"
        self.hostname="localhost"
        self.ReadIP()
        self.save_path = 'class_files/tmp_result/'
        self.Scan()
        self.Compare()

    def ReadIP(self):
        path = os.path.join('class_files/def_ports', self.hostname)
        with open(path, 'r') as file:
            x=file.read().splitlines()
            self.IPaddress=x[0]

    def Scan(self):
        print("Scanning process. Please wait!")
        scan_process.cScan(self.IPaddress, self.hostname, self.save_path)

    def Compare(self):
        print("Compare process")
        compare_process.cCompare(self.hostname)

def main():
    cInit()
if __name__ == "__main__":
    main()