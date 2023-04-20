#! python3
# regexSearch.py - Opens all .txt files in a folder and searches for any line
# that matches a user-supplied regular expression.


import pyinputplus as pyip
import re, shelve


def main():
    # get user regex
    user_regex = get_user_regex()
    # get number of files in a folder
        # open each .txt file in folder
        # read each line in file
        # if user regex in file line
            # print line
    print(user_regex)


def get_user_regex():
    return pyip.inputRegexStr('Enter regex: ')


if __name__ == '__main__':
    main()