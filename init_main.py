from class_files import scan_process

import socket
import os

class cInit:
    def __init__(self):
        self.IPaddress=""   #adres ip celu
        self.hostname=""    #hostname celu
        self.port_range="1-65535"
        self.IP()           #metoda pobierajaca adres ip
        self.Hostname()     #metoda pobierajaca hostname
        self.PortRange()
        self.save_path = "files/default_ports/" + self.hostname # sciezka do zapisania wzorca
        self.save_config_path = "files/config/" + self.hostname
        self.Scan()         #metoda zapisujaca wyniki do pliku
        self.SaveConfig()
        os.system("touch files/report/" + self.hostname)  # stworzenie pliku w ktorym bedzie zapisany raport

    def IP(self):
        while (True):
            address = input("Enter target's IP address: ")
            try:
                socket.inet_aton(address)       #sprawdza poprawnosc adresu ip
            except socket.error:
                print("Invalid input address!")
                continue
            self.IPaddress=address      #zapisanie do zmiennej
            return False

    def Hostname(self):
        while(True):
            hostname= input("Enter target's hostname: ")
            if len(hostname)<1:  #sprawdzenie czy podana zmienna ma zawartosc
                print("Hostname cannot be empty")
                continue
            command='find ./files/config -name "'+hostname+'" | wc -l '  #sprawdzenie czy hostname sie nie powiela
            count=os.popen(command).read()  #wykonanie komendy w konsoli
            if int(count) !=0:
                anwser=input("This hostname already exist! Would You like to overwrite it? N/y: ")
                if anwser=="y":
                    self.hostname=hostname  #ustawienie zmiennej
                    return False    #wyjście z pętli
                else:
                    continue    #zaczecie petli od nowa
            self.hostname=hostname #ustawanie zmiennej
            return False #wyjście z pętli

    def ScanType(self):
        while(True):
            scan_type_disp = {1: "Intense scan plus UDP (Recommended)", 2: "Intense scan", 3: "Quick scan plus"}
            scan_type = {1: "-sS -sU -T4 -A -v", 2: "-T4 -A -v", 3: "-sV -T4 -O -F"}
            for i, j in scan_type_disp.items():
                print(i, j)
            option=input("Scan option: ")
            if not int(option) in range(1, 4):
                print("Invalid input")
                continue
            else:
                self.scan_type=scan_type.get(int(option))
                break

    def PortRange(self):
        decision=input("Default port range 1-65535. Would You like change it? N/y: ")
        if decision=="y":
            first=1
            last=65535
            while (True):
                first = input("Enter first port: ")
                try:
                    int(first)
                except:
                    print("Invalid input, try again!")
                    continue
                if int(first) < 1 or int(first) > 65535:
                    print("Invalid input, try again!")
                    continue
                else:
                    break
            while (True):
                last = input("Enter last port: ")
                try:
                    int(last)
                except:
                    print("Invalid input, try again!")
                    continue
                if int(last) < 1 or int(last) > 65535:
                    print("Invalid input, try again!")
                    continue
                elif first > last:
                    print("First port is higher than last port!")
                else:
                    self.port_range= first + "-" + last
                    break

    def Scan(self):
        print("Scanning process. Please wait!")
        scan_process.cScan(self.IPaddress, self.scan_type, self.port_range)  #proces skanowania wykonany kodem z pliku scan_process.py

    def SaveConfig(self):
        config=self.IPaddress + "\n" + self.scan_type + "\n" + self.port_range
        with open(self.save_config_path, "w+") as file:
            file.write(str(config))

def main():
    cInit()
if __name__ == "__main__":
    main()