#! python3
# textToSheet.py - Reads the contents of several text files and inserts those contents into a spreadsheet.

import openpyxl
from openpyxl.utils import get_column_letter
import sys
import os


def create_workbook():
    # create new workbook
    wb = openpyxl.Workbook()
    sheet = wb.active

    return wb, sheet


def get_files():
    # get files from command line
    args = sys.argv[1:]
    
    # checks that there is at least one command line argument in args list
    if not args:
        args = input("Please include at least one '.txt' file:\n").split(' ')

    # filters list for only '.txt' files
    files = list(filter(lambda f: f.endswith('.txt'), args))

    # checks that there is at least one '.txt' file in files list
    if not files:
        get_files()

    # checks that files exist
    files = check_if_exists(files)
   
    return files


def check_if_exists(files):
    for file in files:
        if not os.path.exists(file):
            files.remove(file)
    return files


def process_files(files):
    for file in files:
        # open each file
        with open(file, encoding='utf-8') as f:
            # read each line of file to get a list of strings
            lines = f.read().splitlines()

        # print(f'{file} lines:\n', lines)



# get current column letter
    # if column A1 contains text, move to next column until blank column found.


# write each string in list to new row of same column


def main():
    wb, sheet = create_workbook()
    files = get_files()
    process_files(files)
    
    return

if __name__ == '__main__':
    main()