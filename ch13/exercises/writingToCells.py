import openpyxl

wb = openpyxl.Workbook()
sheet = wb['Sheet']


# Edit the cell's value
sheet['A1'] = 'Hello, world!'
print(sheet['A1'].value)