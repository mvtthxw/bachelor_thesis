import os
import datetime

class cCompare:
    def __init__(self, hostname):
        self.hostname=hostname
        self.time_now=""
        self.comapre_result=""
        self.report_path = 'files/report/'+ self.hostname
        self.Time()
        self.report = "Day: " + self.time_now + "\n"
        self.Compare()
        self.Save()

    def Time(self):
        now = datetime.datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        time = now.strftime("%H:%M:%S")
        self.time_now = ('{}-{}-{} {}').format(day, month, year, time)

    def Compare(self):
        command="diff files/default_ports/" + self.hostname + " files/tmp_result/" + self.hostname
        self.comapre_result=os.popen(command).read()
        if len(self.comapre_result)==0:
            self.report += "No changes have been detected \n\n"
        else:
            self.Clear()
            self.report += "\n\n"

    def Clear(self):
        for line in self.comapre_result.splitlines():
            if "<" in line:
                self.report += "Port " + line[2:] + " has been closed\n"
            elif ">" in line:
                self.report += "New port " + line[2:] + " has been opened\n"

    def Save(self):
        with open(self.report_path, 'a') as file:
            file.write(str(self.report))
            print(self.report)

