import nmap
import sys


nm=nmap.PortScanner()
#print(sys.argv[1])
address='192.168.1.144'
range='1-443'
#type=sys.argv[2]

nm.scan(address, range)
print(nm[address].state() )

for host in nm.all_hosts():  # lista przeskanowanych hostów
    for protocol in nm[host].all_protocols():  # lista protokołów wykrytych podczas skanowania
        port_list = nm[host][protocol].keys()  # lista portów w danym protokole
        for port in port_list:
            print(port)


#adres='127.0.0.1'
#nm = nmap.PortScanner()
#nm.scan(adres)

#print(nm[adres].state())


