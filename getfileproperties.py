import os
from datetime import datetime

def convert_date(timestamp):
    d = datetime.utcfromtimestamp(timestamp)
    # http://strftime.org/
    formated_date = d.strftime('%c')
    return formated_date


with os.scandir() as dir_entries:
    for entry in dir_entries:
            print(entry.name)
            info = entry.stat()
            print(info)
            # print(convert_date(info.st_mtime))