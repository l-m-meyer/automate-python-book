import openpyxl
from openpyxl.styles import Font


# create blank workbook
wb = openpyxl.Workbook()
sheet = wb['Sheet']


# create font objects
fontObj1 = Font(name='Times New Roman', bold=True)
sheet['A1'].font = fontObj1
sheet['A1'] = 'Bold Times New Roman'


fontObj2 = Font(size=24, italic=True)
sheet['B3'].font = fontObj2
sheet['B3']= '24 pt Italic'


# save to styles workbook
wb.save('styles.xlsx')