import openpyxl


# create blank workbook
wb = openpyxl.Workbook()
sheet = wb.active


# create data for column A
for i in range(1, 11):
    sheet['A' + str(i)] = i


# create reference object
refObj = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)

# create series object
seriesObj = openpyxl.chart.Series(refObj, title='First series')


# create bar chart
chartObj = openpyxl.chart.BarChart()
chartObj.title = 'My Chart'
chartObj.append(seriesObj)


# add bar chart to sheet
sheet.add_chart(chartObj, 'C5')


# save workbook
wb.save('sampleChart.xlsx')