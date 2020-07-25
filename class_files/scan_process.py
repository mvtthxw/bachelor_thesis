import os

class cScan:
    def __init__(self, address, hostname, path):
        self.address=address        #adres celu
        self.hostname=hostname      #hostname
        self.save_path=path         #sciezka do zapisu wyniku
        self.tmp_file=os.path.join('class_files/tmp_scan', "tmp_" + self.hostname)   #sciezka do pliku z surowym wynikiem skanu
        self.save_file = os.path.join(self.save_path, self.hostname)    #sciezka do pliku z przetworzonym wynikiem
        self.scan_result = ''       #zmienna zawierajaca wynik skanu
        self.Scan()                 #proces skanowania
        self.Save(self.tmp_file, "w")    #zapisanie surowego wyniku z nmap do pliku
        self.Clear()                #proces oczyszczania wyniku
        self.Save(self.save_file, "w") #zapisanie przetworzonego wyniku

    def Scan(self):
        command="sudo nmap -sS -sU -T4 -A -v " + self.address #komenda uruchamiajaca nmap
        self.scan_result=os.popen(command).read()   #zapisanie wyniku do zmiennej

    def Clear(self):
        command = 'grep -oE "^[0-9]{1,5}/[a-z]+" ' + self.tmp_file  #komenda wyszukujaca w pliku otwarte porty
        self.scan_result = self.address + "\n" + os.popen(command).read()     #zapisanie wyniku do zmiennej

    def Save(self, file_name, type):
        with open(file_name, type) as file:
            file.write(str(self.scan_result))

