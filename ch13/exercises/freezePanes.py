import openpyxl


# open workbook
wb = openpyxl.load_workbook('..\projects\produceSales.xlsx')
sheet = wb.active


# freeze rows above A2
sheet.freeze_panes = 'A2'


# save workbook
wb.save('freezeExample.xlsx')