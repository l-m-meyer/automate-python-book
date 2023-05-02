import openpyxl


# create new blank workbook
wb = openpyxl.Workbook()
sheet = wb.active


# add values to cells
sheet['A1'] = 200
sheet['A2'] = 300
sheet['A3'] = '=SUM(A1:A2)'     # set the formula


# save workbook
wb.save('writeFormula.xlsx')