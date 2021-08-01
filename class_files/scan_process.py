import nmap

class cScan:
    def __init__(self, address, scan, range):
        self.address=address
        self.scan_type=scan
        self.port_range=range
        self.scan_result = ''       #zmienna zawierajaca wynik skanu
        self.nm = nmap.PortScanner()
        self.nm.scan(self.address, self.port_range, self.scan_type)
        self.Clear()

    def Clear(self):
        for host in self.nm.all_hosts():    #lista przeskanowanych hostów
            for protocol in self.nm[host].all_protocols():     #lista protokołów wykrytych podczas skanowania
                port_list=self.nm[host][protocol].keys()       #lista portów w danym protokole
                for port in port_list:
                    self.scan_result +=  str(port) + "/" + protocol + "\n"


