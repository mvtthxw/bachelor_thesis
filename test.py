import nmap
import sys
nm=nmap.PortScanner()
#print(sys.argv[1])
address=sys.argv[1]
range='1-443'
type=sys.argv[2]
print(type)
nm.scan(address, range, type)

for host in nm.all_hosts():  # lista przeskanowanych hostów
    for protocol in nm[host].all_protocols():  # lista protokołów wykrytych podczas skanowania
        port_list = nm[host][protocol].keys()  # lista portów w danym protokole
        for port in port_list:
            print(port)