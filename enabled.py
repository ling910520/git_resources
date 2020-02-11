import threading
import time
import code
from os import system
class continous_print():
    def __init__(self):
        self.enabled = False
        self.serverThread = None
        self.stopServerThread = False
        self.serverSock = None
    def enable(self):
        if not self.enabled:
            self.enabled = True
            self.__start_server_thread()
    def disable(self):
        if self.enabled:
            self.enabled = False
            if  self.serverThread.is_alive():
                self.stopServerThread = True
                # wait for connection thread to stop
                # while self.stopServerThread:
                #     time.sleep(0.2)
    def __start_server_thread(self):
        self.serverThread = threading.Thread(target = self.__server_thread,name="server start",daemon=True)
        self.serverThread.start()
        # while self.serverThread.is_alive():
        #     self.serverThread.join(1)
    def __server_thread(self):
       self.cnt = 0
       while not self.stopServerThread:
            try:
                print(f"count is {self.cnt}")
                with open("test.txt", 'a') as f:
                    f.write(f"count is {self.cnt}"+ "\n")
                time.sleep(2)
                self.cnt += 1
            except:
                continue

                
            
if __name__ == '__main__':
        system("title "+"myCoolTitle")
        h = continous_print()
        h.enable()
        code.interact("host object is available as variable 'h'", local=locals())

