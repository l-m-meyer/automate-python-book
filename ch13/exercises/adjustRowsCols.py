import openpyxl


# create blank workbook
wb = openpyxl.Workbook()
sheet = wb.active


# set cell values
sheet['A1'] = 'Tall row'
sheet['B2'] = 'Wide column'


# set height and width
sheet.row_dimensions[1].height = 70
sheet.column_dimensions['B'].width = 20


# save workbook
wb.save('dimensions.xlsx')