import openpyxl
from openpyxl.styles import Font


# create blank workbook
wb = openpyxl.Workbook()
sheet = wb['Sheet']


# create font
italic24Font = Font(size=24, italic=True)


# apply font to cell A1
sheet['A1'].font = italic24Font
sheet['A1'] = 'Hello world!'


# save workbook
wb.save('styles.xlsx')