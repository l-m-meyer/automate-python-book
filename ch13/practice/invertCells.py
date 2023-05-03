#! python3
# invertCells.py - Inverts the row and column of the cells in a spreadsheet.


import openpyxl, random


def create_sample_data():
    # create blank workbook
    wb = openpyxl.Workbook()
    sheet = wb.active


    # enter data into blank workbook
    sheet['A1'] = 'ITEM'
    sheet['B1'] = 'SOLD'

    items = ['Eggplant', 'Cucumber', 'Cabbage', 'Garlic', 'Parsnips', 'Asparagus', 'Brussel Sprouts']

    for i, item in enumerate(items):
        ran = random.randint(1, 500)
        
        sheet[f'A{i + 2}'].value = item
        sheet[f'B{i + 2}'].value = ran


    # save workbook
    filename = 'sampledata.xlsx'
    wb.save(filename)

    return filename


# TODO: invert cells from sheet[x][y] to sheet[y][x]
def invert_cells():
    pass


# TODO: load file to invert
def load_file(filename):
    pass


def main():
    filename = create_sample_data()
    load_file(filename)


if __name__ == '__main__':
    main()