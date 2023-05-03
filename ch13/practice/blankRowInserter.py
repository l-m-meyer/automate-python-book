#! python3
# blankRowInserter.py - Starting at row N, inserts M blank rows into a spreadsheet.


import openpyxl, sys
from openpyxl.utils import get_column_letter


# get arguments from command line
try:
    starting_row = int(sys.argv[1])
    num_blank_rows = int(sys.argv[2])
    filename = sys.argv[3]
except IndexError as e:
    print('You are missing arguments.\nError:', e)


# open workbook
wb = openpyxl.load_workbook(filename, data_only=True)
sheet = wb.active


# add number of blank rows in spreadsheet
sheet.insert_rows(starting_row, amount=num_blank_rows)

# save workbook
wb.save('fileWithBlanks.xlsx')