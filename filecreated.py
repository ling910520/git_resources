import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.utils import BaseThread
import os
from shutil import copytree,copy

DIRECTORY_TO_WATCH = r"C:\Users\ling910520\Desktop\py\resources"
base= r"C:\Users\ling910520\Desktop"
class Watcher:

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    def on_created(self,event):
       
        if event.is_directory:            
            foldername=os.path.relpath(event.src_path,DIRECTORY_TO_WATCH)
            pathname = os.path.dirname(event.src_path)
            check = Helper()
            if check.checkSize(event.src_path):#check filesize increase
                self.copytree(foldername,pathname)
            
            
        else:
            filename=os.path.relpath(event.src_path,DIRECTORY_TO_WATCH)
            pathname = os.path.dirname(event.src_path)
            check = Helper()
            if check.checkSize(event.src_path): #check filesize increase
                self.copyfile(filename,pathname)
            

    @staticmethod
    def copytree(foldername,pathname):
        src  = os.path.join(DIRECTORY_TO_WATCH,foldername)
        dst = os.path.join(base,foldername)
        copytree(src,dst)

    @staticmethod
    def copyfile(filename,pathname):
        src  = os.path.join(DIRECTORY_TO_WATCH,filename)
        dst = os.path.join(base,filename)
        copy(src,dst)


class Helper:
    @staticmethod 
    def checkSize(path):
        historicalSize=-1
        while (historicalSize != os.path.getsize(path)):
            historicalSize = os.path.getsize(path)
            time.sleep(1)
        
        print("file size not increase anymore")
        return True

class test(BaseThread):
    def __init__(self):
            BaseThread.__init__(self)
            # self._original_run = self.run
            # self.run = self.run_wrapper
    # def run_wrapper(self):
    #     try:
    #         self._original_run()
    #     except Exception:
    #         print("error")
    #         # self.queue.put(e)

    def on_thread_start(self):
        print("start process raw files")

    #         print("thread stop or Error")
            
    # def on_thread_stop(self):
    #     print("end process raw files")


if __name__ == '__main__':
    # w = Watcher()
    # w.run()
    t = test()
    t.start()