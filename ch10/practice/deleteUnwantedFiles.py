#! python3
# deleteUnwantedFiles.py - Find and delete large, unwanted files of more than 100MB.


import pyinputplus as pyip
import os


def get_folder():
    folder = pyip.inputFilepath('Enter a filepath for folder to copy: ', mustExist=True)

    if not os.path.exists(folder):
        print('Filepath is invalid.')
        return get_folder()
    
    return os.path.abspath(folder)


def main():
    folder = get_folder()
    pass


if __name__ == "__main__":
    main()