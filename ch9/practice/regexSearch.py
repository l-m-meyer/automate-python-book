#! python3
# regexSearch.py - Opens all .txt files in a folder and searches for any line
# that matches a user-supplied regular expression.

import pprint as pp
import pyinputplus as pyip
from pathlib import Path
import re, os


def main():
    user_regex = get_user_regex()
    user_path = get_user_path()
    matches = search_files(user_regex, user_path)
    
    pp.pprint(matches)


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
    # lists all files in filepath
    files = os.listdir(fpath)
    matches = []
    for file in files:
        if not file.endswith('.txt'):
            continue
        # open each .txt file in folder
        with open(fpath / file) as f:
            # read each line in file and add match to matches list
            for line in f.readlines():
                for match in re.findall(pattern, line):
                    matches.append({'match': match,
                                    'line': line,
                                    'file': file
                                    })
    return matches


if __name__ == '__main__':
    main()