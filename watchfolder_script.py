import subprocess, os, re, time, shutil
from script_1 import *

watch_path = "/Users/ingest1/Movies/TEMP/HDR/Script_IN/"

print("Watching folder...")
while True:
    time.sleep(5)
    file_list = os.listdir(watch_path)

    for file in file_list:
        if file == '.DS_Store':
            pass
        else:
            print("Found new file")
            print("Encoding " + file)
            current_size = getSize(file)
            print( 'Current size is ' + str(current_size) + ' bytes')
            time.sleep(5)
            while current_size != getSize(file):
                current_size = getSize(file)
                print('Current size is {} bytes'.format(current_size))
                time.sleep(10)
            run(file)
            print("Watching folder...")
