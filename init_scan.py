from class_files import first_scanner

import threading

class cFirstMain:
    def __init__(self):
        self.host_objects=[]
        self.threads_list=[]
        self.InputProcess()
        self.ScanProcess()
        print("Scanning process have been done.")

    def InputProcess(self):
        con='y'
        while con=='y':
            host=first_scanner.cFirstScanner()
            self.host_objects.append(host)
            con=input("Do you want add new host - type y: ")

    def ScanProcess(self):
        print("Scanning process. Please wait!")
        for host in self.host_objects:
            thread = threading.Thread(target=host.CheckStatus())
            thread.start()
            self.threads_list.append(thread)
        for thread in self.threads_list:
            thread.join()


def main():
    cFirstMain()

if __name__ == "__main__":
    main()