#! python3
# tablePrinter.py - Displays a table with each column right-justified.


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
    colWidth = []
    
    for el in data:
        # Adds the length of the longest string to the colWidth list
        colWidth.append(len(max(el, key=len)))
       
    # For loop to decide the determine the number of columns to cycle through
    for x, col in enumerate(data[0]):
        # For loop for the number of rows to cycle through
        for y, row in enumerate(data): 
            # Print each row data with the correct justification        
            print(data[y][x].rjust(colWidth[y]), end=' ')
        # Create a new line before reiterating
        print('')

printTable(tableData)