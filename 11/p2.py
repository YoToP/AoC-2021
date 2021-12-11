from time import time
def findAdjecent(matrix, i,j):
    total = 1
    matrix[i][j] = 11

    #update and check up/left
    if (i - 1 >= 0) and (j - 1 >= 0): #check out of bounds
        if matrix[i-1][j-1] == 0:None
        elif matrix[i-1][j-1] < 9: matrix[i-1][j-1] += 1 
        elif matrix[i-1][j-1] == 9: total += findAdjecent(matrix,i-1,j-1)
    #check up
    if i - 1 >= 0: #check out of bounds
        if matrix[i-1][j] == 0:None
        elif matrix[i-1][j] < 9: matrix[i-1][j] += 1
        elif matrix[i-1][j] == 9: total += findAdjecent(matrix,i-1,j)
    #check up/right
    if (i - 1 >= 0) and (j + 1 < len(matrix[i])): #check out of bounds
        if matrix[i-1][j+1] == 0:None
        elif matrix[i-1][j+1] < 9: matrix[i-1][j+1] += 1
        elif matrix[i-1][j+1] == 9: total += findAdjecent(matrix,i-1,j+1)
    #check left
    if j - 1 >= 0: #check out of bounds
        if matrix[i][j-1] == 0:None
        elif matrix[i][j-1] < 9: matrix[i][j-1] += 1
        elif matrix[i][j-1] == 9: total += findAdjecent(matrix,i,j-1)
    #check right
    if j + 1 < len(matrix[i]): #check out of bounds
        if matrix[i][j+1] == 0:None
        elif matrix[i][j+1] < 9: matrix[i][j+1] += 1
        elif matrix[i][j+1] == 9: total += findAdjecent(matrix,i,j+1)
    #check down/left
    if (i + 1 < len(matrix)) and (j - 1 >= 0): #check out of bounds
        if matrix[i+1][j-1] == 0:None
        elif matrix[i+1][j-1] < 9: matrix[i+1][j-1] += 1
        elif matrix[i+1][j-1] == 9: total += findAdjecent(matrix,i+1,j-1)
    #check down
    if i + 1 < len(matrix): #check out of bounds
        if matrix[i+1][j] == 0:None
        elif matrix[i+1][j] < 9: matrix[i+1][j] += 1
        elif matrix[i+1][j] == 9: total += findAdjecent(matrix,i+1,j)
    #check down/right
    if (i + 1 < len(matrix)) and (j + 1 < len(matrix[i])): #check out of bounds
        if matrix[i+1][j+1] == 0:None
        elif matrix[i+1][j+1] < 9: matrix[i+1][j+1] += 1
        elif matrix[i+1][j+1] == 9: total += findAdjecent(matrix,i+1,j+1)
    matrix[i][j] = 0
    return total


def solvep2(path,rounds):
    with open(path) as f:
        lines = f.readlines()
    matrix = []
    height = 0
    width = 0
    for line in lines: # load playing field into matrix
        height += 1
        line = line.replace('\n', '')
        width = len(line)
        lstLine = []
        for nr in line:
            lstLine.append(int(nr))
        matrix.append(lstLine)
    
    mustflash = width * height
    roundsLeft = rounds
    while roundsLeft > 0:
        total = 0
        #check every single element, when lower than 9. perform recursive function and overwrite number with 10 and increase basin size
        for i in range(height):
            for j in range(width):
                #update this tile
                if matrix[i][j] > 8:
                    matrix[i][j] = 10
                else:
                    matrix[i][j] += 1
        for i in range(height):
            for j in range(width):
                #find all updates
                if matrix[i][j] == 10:
                    total += 1
                    matrix[i][j] += 1
                    #update and check up/left
                    if (i - 1 >= 0) and (j - 1 >= 0): #check out of bounds
                        if matrix[i-1][j-1] == 0:None
                        elif matrix[i-1][j-1] < 9: matrix[i-1][j-1] += 1 
                        elif matrix[i-1][j-1] == 9: total += findAdjecent(matrix,i-1,j-1)
                    #check up
                    if i - 1 >= 0: #check out of bounds
                        if matrix[i-1][j] == 0:None
                        elif matrix[i-1][j] < 9: matrix[i-1][j] += 1
                        elif matrix[i-1][j] == 9: total += findAdjecent(matrix,i-1,j)
                    #check up/right
                    if (i - 1 >= 0) and (j + 1 < len(matrix[i])): #check out of bounds
                        if matrix[i-1][j+1] == 0:None
                        elif matrix[i-1][j+1] < 9: matrix[i-1][j+1] += 1
                        elif matrix[i-1][j+1] == 9: total += findAdjecent(matrix,i-1,j+1)
                    #check left
                    if j - 1 >= 0: #check out of bounds
                        if matrix[i][j-1] == 0:None
                        elif matrix[i][j-1] < 9: matrix[i][j-1] += 1
                        elif matrix[i][j-1] == 9: total += findAdjecent(matrix,i,j-1)
                    #check right
                    if j + 1 < len(matrix[i]): #check out of bounds
                        if matrix[i][j+1] == 0:None
                        elif matrix[i][j+1] < 9: matrix[i][j+1] += 1
                        elif matrix[i][j+1] == 9: total += findAdjecent(matrix,i,j+1)
                    #check down/left
                    if (i + 1 < len(matrix)) and (j - 1 >= 0): #check out of bounds
                        if matrix[i+1][j-1] == 0:None
                        elif matrix[i+1][j-1] < 9: matrix[i+1][j-1] += 1
                        elif matrix[i+1][j-1] == 9: total += findAdjecent(matrix,i+1,j-1)
                    #check down
                    if i + 1 < len(matrix): #check out of bounds
                        if matrix[i+1][j] == 0:None
                        elif matrix[i+1][j] < 9: matrix[i+1][j] += 1
                        elif matrix[i+1][j] == 9: total += findAdjecent(matrix,i+1,j)
                    #check down/right
                    if (i + 1 < len(matrix)) and (j + 1 < len(matrix[i])): #check out of bounds
                        if matrix[i+1][j+1] == 0:None
                        elif matrix[i+1][j+1] < 9: matrix[i+1][j+1] += 1
                        elif matrix[i+1][j+1] == 9: total += findAdjecent(matrix,i+1,j+1)
                    matrix[i][j] = 0
        roundsLeft -= 1
        if mustflash == total:
            return rounds - roundsLeft
    return 0

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print(solvep2("11/input.txt"))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))