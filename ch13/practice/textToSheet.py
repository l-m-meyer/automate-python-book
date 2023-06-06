#! python3
# textToSheet.py - Reads the contents of several text files and inserts those contents into a spreadsheet.

import openpyxl
from openpyxl.utils import get_column_letter
import sys


def create_workbook():
    # create new workbook
    wb = openpyxl.Workbook()
    sheet = wb.active

    return wb, sheet


def get_files():
    # get files from command line
    args = sys.argv[1:]

    # filters list for only '.txt' files
    files = list(filter(lambda f: f.endswith('.txt'), args))
    
    return files


# open each file


# read each line of file to get a list of strings


# get current column letter
    # if column A1 contains text, move to next column until blank column found.


# write each string in list to new row of same column


def main():
    wb, sheet = create_workbook()
    files = get_files()
    return

if __name__ == '__main__':
    main()