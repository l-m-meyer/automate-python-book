#! python3
# treewalk.py


import os


for folderName, subFolders, fileNames in os.walk('C:\\delicious'):
    print(f'The current folder is {folderName}')


    for subfolder in subFolders:
        print(f'SUBFOLDER OF {folderName}: {subfolder}')


    for filename in fileNames:
        print(f'FILE INSIDE {folderName}: {filename}')


    print('')