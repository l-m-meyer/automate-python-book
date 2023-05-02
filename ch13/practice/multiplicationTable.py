#! python3
# multiplicationTable.py - Creates a NxN multiplication table in an Excel spreadsheet.


import openpyxl, sys
import pyinputplus as pyip


# create blank workbook
wb = openpyxl.Workbook()
sheet = wb.active


# get number N from the command line
try:
    n = sys.argv[1]
except IndexError as e:
    print('Forget something? A number perhaps?\nError:', e)
    print()
    print('Try again...')
    n = pyip.inputInt('Enter a number: ')


# TODO: create column and row headers in bold


# TODO: add formula to calculate values for each cell


# TODO: save workbook