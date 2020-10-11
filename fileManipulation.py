
# A file for testing new stuff

import os
import time

f = open("demofile.txt", "w")
f.write("Sup brah")
f.close()

if os.path.exists("demofile.txt"):
    f = open("demofile.txt", "r")
    print(f.read())
    f.close()
    print("removing file...")
    for i in range(3):
        time.sleep(1)
        print(".")
    os.remove("demofile.txt")
    print("file has been removed")
else:
    print("the file does not exist")
