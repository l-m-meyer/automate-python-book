#! python3
# textToSheet.py - Reads the contents of several text files and inserts those contents into a spreadsheet.

import openpyxl
from openpyxl.utils import get_column_letter
import sys


# create new workbook
def create_workbook():
    wb = openpyxl.Workbook()
    sheet = wb.active

    return sheet


# get files


# open file


# read each line of file to get a list of strings


# get current column letter
    # if column A1 contains text, move to next column until blank column found.


# write each string in list to new row of same column


def main():
    return

if __name__ == '__main__':
    main()