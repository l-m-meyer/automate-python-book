#! python3
# regexSearch.py - Opens all .txt files in a folder and searches for any line
# that matches a user-supplied regular expression.


import pyinputplus as pyip
from pathlib import Path
import re, os


def main():
    user_regex = get_user_regex()
    user_path = get_user_path()
    search_files(user_regex, user_path)
    
    return


def get_user_regex():
    return pyip.inputRegexStr('Enter regex: ')


def get_user_path():
    path = pyip.inputStr('Enter filepath: ')
    basedir = Path(path)

    if not basedir.is_dir():
        print('Path invalid.')
        return get_user_path()
    
    return basedir


def search_files(pattern, fpath):
    files = os.listdir(fpath)
    
    for file in files:
        if file.endswith('.txt'):
            # open each .txt file in folder
            print(file)
            # read each line in file
            # if user regex in file line
                # print line
    return


if __name__ == '__main__':
    main()