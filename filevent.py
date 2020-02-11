import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    DIRECTORY_TO_WATCH = "../resources"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    def on_any_event(self,event):
       
        if event.is_directory:
            self.helpDirectory(event)
        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event - %s." % event.src_path)

        elif event.event_type == 'modified':
            # Taken any action here when a file is modified.
            print("Received modified event - %s." % event.src_path)
    @staticmethod
    def helpDirectory(event):
        if event.event_type == 'created':
            print("Directory Created {}".format(event.src_path))
        elif event.event_type == 'modified':
             print("Directory modified {}".format(event.src_path))

if __name__ == '__main__':
    w = Watcher()
    w.run()