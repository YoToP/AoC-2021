def rowBingo(board):
    for i in range(5):
        rowBingo = 0
        for j in range(5):
            if board[i][j][1] == True:
                rowBingo += 1
                if rowBingo == 5:
                    return True
    return False

def columnBingo(board):
    for i in range(5):
        columnBingo = 0
        for j in range(5):
            if board[j][i][1] == True:
                columnBingo += 1
                if columnBingo == 5:
                    return True
    return False

def sumUnmarked(board):
    sum = 0
    for i in range(5):
        for j in range(5):
            if board[j][i][1] == False:
                sum += board[j][i][0]
    return sum

def solvep1(path):
    with open(path) as f:
        lines = f.readlines()
    #Create boards 5x5
    lstBoards = []
    #number on each board is a tuple (#, boolean)
    bFirstLine = True
    lstChosenNumbers = []
    for line in lines:
        if not bFirstLine:
            if len(line) < 10: #Reset administration on empty line
                _rowCount = 0
                _lstBoard = [[],[],[],[],[]]
            if len(line) >= 10:#skip empty rows
                _lineElements = line.split(" ")#causes problem with single digits
                _filtertLineElements = [] # so we need an array with filtered elements. 
                for lineElement in _lineElements:
                    if lineElement != '': # filter by removing empty elements in the text
                        _filtertLineElements.append((int(lineElement),False)) #and add the tuple with a False bit, used for the score
                _lstBoard[_rowCount] = _filtertLineElements.copy()
                _rowCount += 1
                if _rowCount == 5:
                    lstBoards.append(_lstBoard.copy())
        if bFirstLine:#read chosen numbers on first line
            lstChosenNumbers = line.split(",")
            bFirstLine = False
    #all boards loaded
    for _number in lstChosenNumbers:
        for i in range(len(lstBoards)):
            #mark chosen nr
            for x in range(5):
                for y in range(5):
                    _scratch = lstBoards[i][x][y][0]
                    if lstBoards[i][x][y][0] == int(_number):
                        lstBoards[i][x][y] = (int(_number),True)
            
            if rowBingo(lstBoards[i]) or columnBingo(lstBoards[i]):
                return sumUnmarked(lstBoards[i])*int(_number)
    return 0

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    print(solvep1("4/input.txt"))