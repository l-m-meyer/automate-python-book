import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
wb.sheetnames
# ['Sheet1', 'Sheet2', 'Sheet3']

sheet = wb['Sheet3']    # Get a sheet from the workbook
type(sheet)
# <class 'openpyxl.worksheet.worksheet.Worksheet'>

sheet.title             # Get sheet's title as a string
# 'Sheet3'

anotherSheet = wb.active    # Get the active sheet
# <Worksheet "Sheet1">