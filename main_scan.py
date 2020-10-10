from class_files import scanner

import threading
import os

class cMain:
    def __init__(self):
        self.target_list=[]
        self.threads_list=[]
        self.ReadTargets()
        self.RunThreads()

    def ReadTargets(self):
        command = "ls files/config"
        self.target_list = os.popen(command).read().splitlines()
        print(self.target_list)

    def RunThreads(self):
        for host in self.target_list:
            thread = threading.Thread(target=self.Daemon, args=(host,))
            thread.start()
            self.threads_list.append(thread)
        for thread in self.threads_list:
            thread.join()

    def Daemon(self, host):
        scanner.cScanner(host)

def main():
    cMain()

if __name__ == "__main__":
    main()