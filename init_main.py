#wykonanie pierwszego skanu z ktorego powstanie wzorzec
from class_files import scan_process

import socket
import os

class cInit: #tworzenie klasy
    def __init__(self):
        self.IPaddress=""   #adres ip celu
        self.hostname=""    #hostname celu
        self.IP()           #metoda pobierajaca adres ip
        self.Hostname()     #metoda pobierajaca hostname
        self.save_path='class_files/def_ports/' #sciezka do zapisania wzorca
        self.Scan()         #metoda zapisujaca wyniki do pliku
        os.system("touch ./class_files/raport/" + self.hostname)  # stworzenie pliku w ktorym bedzie zapisany raport

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
            command='find ./class_files/def_ports -name "'+hostname+'" | wc -l '  #sprawdzenie czy hostname sie nie powiela
            count=os.popen(command).read()
            if int(count) !=0:
                print("This hostname already exist")
            else:
                self.hostname=hostname #ustawanie zmiennej
                return False
    def Scan(self):
        print("Scanning process. Please wait!")
        scan_process.cScan(self.IPaddress, self.hostname, self.save_path)  #proces skanowania wykonany kodem z pliku scan_process.py

def main():
    cInit()
if __name__ == "__main__":
    main()