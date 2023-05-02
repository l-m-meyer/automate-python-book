#! python3
# readCensusExcel.py - Tabulates population and number of census tracts for each county.

"""
- Reads the data from the Excel spreadsheet
- Counts the number of census tracts in each county
- Counts the total population of each county
- Prints the results
"""

import openpyxl, pprint


print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']

countyData = {}

# TODO: Fill in the countyData with each county's population and tracts.
print('Reading rows...')

for row in range(2, sheet.max_row + 1):
    # Each row in the spreadsheet has data for one census tract.
    state   = sheet['B' + str(row)].value
    county  = sheet['C' + str(row)].value
    pop     = sheet['D' + str(row)].value


# TODO: Open a new text file and write the contents of countyData to it.