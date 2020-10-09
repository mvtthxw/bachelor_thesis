import datetime

class cSave:
    def __init__(self, hostname, report):
        self.hostname=hostname
        self.report=report
        self.report_path="files/report/" + self.hostname
        self.time_now=""
        self.GenDate()
        self.Save()

    def GenDate(self):
        now = datetime.datetime.now()
        year = now.strftime("%Y")
        month = now.strftime("%m")
        day = now.strftime("%d")
        time = now.strftime("%H:%M:%S")
        self.time_now = ('{}-{}-{} {}').format(day, month, year, time)

    def Save(self):
        with open(self.report_path, 'a') as file:
            file.write(str(self.time_now + "\n" + self.report + "\n\n"))
