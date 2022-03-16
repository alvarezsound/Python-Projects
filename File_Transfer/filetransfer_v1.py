import os,time
import datetime
import shutil

import datetime as dt

now = dt.datetime.now()
ago = now-dt.timedelta(hours=24)
strftime = "%H:%M %m/%d/%Y"
src = '/Users/jeff/Documents/GitHub/Python-Projects/File_Transfer/Files'
dst = '/Users/jeff/Documents/GitHub/Python-Projects/File_Transfer/Transfer'

for root, dirs,files in os.walk(src):  
    for fname in files:
        path = os.path.join(root, fname)
        st = os.stat(path)    
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
            print("Moved:", fname, " modified within 24 hours at", mtime.strftime("%H:%M %m/%d/%Y"))
            shutil.move(path, dst)
