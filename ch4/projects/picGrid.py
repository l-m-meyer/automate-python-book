grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def showPic(grid):
    # Iterates from 0 to 6 to get column value
    for y in range(len(grid[0])):
        # Iterates from 0 to 9 to get row value
        for x in range(len(grid)):
            print(grid[x][y], end='')
        print()

showPic(grid)