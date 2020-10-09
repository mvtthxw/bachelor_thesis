from class_files import scan_process
from class_files import compare_process
from class_files import read_process
from class_files import save_process

import nmap

class cInit:
    def __init__(self, hostname):
        self.hostname = hostname
        self.IPaddress=""
        self.scan_type=""
        self.port_range=""
        self.scan_result =""
        self.report=""
        self.Read()
        self.CheckStatus()
        self.Save()

    def Read(self):
        oRead=read_process.cRead(self.hostname)
        self.IPaddress=oRead.IPaddress
        self.scan_type=oRead.scan_type
        self.port_range=oRead.port_range

    def CheckStatus(self):
        nm = nmap.PortScanner()
        nm.scan(self.IPaddress)
        if len(nm.all_hosts())==0:
            self.report="Host is down"
        else:
            self.Scan()
            self.Compare()

    def Scan(self):
        print("Scanning process. Please wait!")
        oScan=scan_process.cScan(self.IPaddress, self.scan_type, self.port_range)
        self.scan_result=oScan.scan_result

    def Compare(self):
        print("Compare Process")
        oCompare=compare_process.cCompare(self.hostname, self.scan_result)
        self.report=oCompare.compare_result

    def Save(self):
        save_process.cSave(self.hostname, self.report)
