import threading, time

class reqthread(threading.Thread):    
    def run(self):
        for i in range(0, 10):
            time.sleep(1)
            print('.')

try:
    thread = reqthread()
    thread.start()
    while thread.isAlive(): 
        thread.join(1)  # not sure if there is an appreciable cost to this.
except (KeyboardInterrupt, SystemExit):
    print('\n! Received keyboard interrupt, quitting threads.\n')