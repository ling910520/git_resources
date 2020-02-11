from shutil import copytree
import os
import time

src=r"C:\Users\ling910520\Desktop\py\resources\test"
dst=r"C:\Users\ling910520\Desktop\py\resources\test1"
#dst = os.path.join(os.path.dirname(src),"New folder")

# print(os.path.basename(src))
copytree(src, dst)

time.sleep(5000)