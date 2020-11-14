from difflib import Differ

class cCompare:
    def __init__(self, hostname, scan_result):
        self.hostname=hostname
        self.scan_result=scan_result.splitlines()
        self.template_scan=''
        self.compare_result=''
        self.template_path = 'files/default_ports/'+ self.hostname
        self.monitoring_path = "files/monitoring/" + self.hostname
        self.ReadTemplate()
        self.Compare()

    def ReadTemplate(self):
        with open(self.template_path, 'r') as file:
            self.template_scan=file.read().splitlines()

    def Compare(self):
        dif = Differ()
        compare = list(dif.compare(self.template_scan, self.scan_result))
        for line in compare:
            if line[0] == '+':
                self.compare_result += "New port " + line[2:] + " has been opened\n"
            elif line[0] == '-':
                self.compare_result += "Port " + line[2:] + " has been closed\n"
        if len(self.compare_result)==0:
            self.compare_result="No changes have been detected"
            with open(self.monitoring_path, "w+") as file:
                file.write(str(1))
        else:
            with open(self.monitoring_path, "w+") as file:
                file.write(str(0))

