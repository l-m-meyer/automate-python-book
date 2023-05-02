#! python3
# blankRowInserter.py - Starting at row N, inserts M blank rows into a spreadsheet.


import openpyxl, sys


# get arguments from command line
try:
    row = sys.argv[1]
    num_blank_rows = sys.argv[2]
    filename = sys.argv[3]
except IndexError as e:
    print('You are missing arguments.\nError:', e)


# open workbook
wb = openpyxl.Workbook()
sheet = wb.active


# TODO: copy first lines from 1 to row


# TODO: add number of blank rows in spreadsheet


# save workbook
wb.save('fileWithBlanks.xlsx')