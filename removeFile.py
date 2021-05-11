import os
import shutil
import time
import datetime

path = input("Enter your path here: ")

if(os.path.exists(path)):
    creation_day = datetime.datetime.fromtimestamp(os.path.getctime(path))
    current_day = datetime.datetime.now()
    age = current_day - creation_day

    if(int(age.days) > 365):
        os.remove(path)