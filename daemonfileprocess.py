import filecreated
import daemon
import time

a = filecreated.Watcher()

# def run():
#     with daemon.DaemonContext():
#         a

if __name__ == "__main__":
    a.run()