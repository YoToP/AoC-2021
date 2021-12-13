from time import time
from collections import defaultdict
from copy import deepcopy
def solvep2(path):
    with open(path) as f:
        lines = f.readlines()
    grid = defaultdict(lambda: defaultdict(int))
    
    bFoldInstructions = False
    for line in lines:
        line = line.replace('\n', '')
        if line == '':bFoldInstructions = True
        elif not bFoldInstructions:
            x, y = line.split(',') #x is to the right, y is down
            grid[int(y)][int(x)] += 1
        else:
            coord, foldLinePos = line.split(' ')[2].split('=')
            foldLinePos = int(foldLinePos)
            if coord == 'y':
                _copyGrid = deepcopy(grid)
                for _row, _grid in _copyGrid.items():
                    if _row > foldLinePos:
                        for _column, _x in _grid.items(): 
                            grid[foldLinePos-(_row - foldLinePos)][_column] += 1
                        del grid[_row]
                    
            elif coord == 'x':
                _copyGrid = deepcopy(grid)
                for _row, _grid in _copyGrid.items():
                    for _column, _x in _grid.items(): 
                        if _column > foldLinePos:
                            grid[_row][foldLinePos -(_column-foldLinePos)] += 1
                        if _column > foldLinePos: 
                            del grid[_row][_column]

    maxRow = 0
    maxColumn = 0
    for _row, _grid in grid.items():
        if _row > maxRow:maxRow = _row
        for _column, _x in _grid.items():
            if _column > maxColumn:maxColumn = _column
    stringlines = []
    for i in range(maxRow+1):
        _string = []
        for j in range(maxColumn+1):
            _string.append(' ')
        stringlines.append(_string)
    for _row, _grid in grid.items():
        for _column, _x in _grid.items():
            stringlines[_row][_column] = chr(9608) #unicode for block
    

    for _string in stringlines:
        print("".join(_string))
    return 0

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    solvep2("13/input.txt")
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))