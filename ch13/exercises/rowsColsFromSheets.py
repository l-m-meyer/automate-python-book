import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']
print(tuple(sheet['A1':'C3']))             # Get all cells from A1 to C3; Generator object

for rowOfCellOjbects in sheet['A1':'C3']:
    for cellObj in rowOfCellOjbects:
        print(cellObj.coordinate, cellObj.value)
    print('--- END OF ROW ---')


sheet = wb.active
list(sheet.columns)[1]                     # Get second column's cells

for cellObj in list(sheet.columns)[1]:
    print(cellObj.value)