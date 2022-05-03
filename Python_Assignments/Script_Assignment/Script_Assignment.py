import os
import time

fPath = '/Users/jeff/Documents/GitHub/Python-Projects/Script_Assignment/'
ext = ('.rtf')
for files in os.listdir(fPath):
    f = os.path.join(fPath, files)
    modification_time = os.path.getmtime(f)
    if files.endswith(ext):
        print(f, modification_time)  
    else:
        continue


