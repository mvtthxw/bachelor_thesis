import os
import datetime

class cCompare:
    def __init__(self, hostname):
        self.hostname=hostname
        self.time_now=""
        self.comapre_result=""
        self.Time()
        self.raport = "Day: " + self.time_now + "\n"
        self.Compare()
        self.Save()
        print(self.raport)

    def Time(self):
        now = datetime.datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        time = now.strftime("%H:%M:%S")
        self.time_now = ('{}-{}-{} {}').format(day, month, year, time)

    def Compare(self):
        command="diff class_files/def_ports/" + self.hostname + " class_files/tmp_result/" + self.hostname
        self.comapre_result=os.popen(command).read()
        if len(self.comapre_result)==0:
            self.raport = self.raport + "No changes have been detected \n\n"
        else:
            self.Clear()

    def Clear(self):
        for line in self.comapre_result.splitlines():
            if "<" in line:
                self.raport = self.raport + "Port " + line[2:] + " has been closed\n"
            elif ">" in line:
                self.raport = self.raport + "New port " + line[2:] + " has been opened\n"

    def Save(self):
        path = os.path.join('class_files/raport', self.hostname)
        with open(path, 'a') as file:
            file.write(str(self.raport))


