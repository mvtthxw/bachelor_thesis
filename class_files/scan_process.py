import nmap

class cScan:
    def __init__(self, address, scan, range, path):
        self.address=address        #adres celu
        self.scan_type=scan
        self.port_range=range
        self.save_path= path         #sciezka do zapisu wyniku
        self.scan_result = ''       #zmienna zawierajaca wynik skanu
        self.nm = nmap.PortScanner()
        self.nm.scan(self.address, self.port_range, self.scan_type)
        self.Clear()                #proces oczyszczania wyniku
        self.Save()#zapisanie przetworzonego wyniku


    def Clear(self):
        for host in self.nm.all_hosts():    #lista przeskanowanych hostów
            for protocol in self.nm[host].all_protocols():     #lista protokołów wykrytych podczas skanowania
                port_list=self.nm[host][protocol].keys()       #lista portów w danym protokole
                for port in port_list:
                    self.scan_result +=  str(port) + "/" + protocol + "\n"

    def Save(self):
        with open(self.save_path, "w+") as file:
            file.write(str(self.scan_result))
            print(self.scan_result)

#cScan("172.20.10.11", "-sS -sU -T4 -A -v", "21-443", "hello")