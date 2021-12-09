from time import time
def findAdjecent(matrix, i,j):
    intBasinSize = 0
    if matrix[i][j] < 9:
        intBasinSize = 1
        matrix[i][j] = 10
        #check up
        if i - 1 >= 0: #check out of bounds
            intBasinSize += findAdjecent(matrix,i-1,j)
        #check left
        if j - 1 >= 0: #check out of bounds
            intBasinSize += findAdjecent(matrix,i,j-1)
        #check right
        if j + 1 < len(matrix[i]): #check out of bounds
            intBasinSize += findAdjecent(matrix,i,j+1)
        #check down
        if i + 1 < len(matrix): #check out of bounds
            intBasinSize += findAdjecent(matrix,i+1,j)
    return intBasinSize


def solvep2(path):
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

    basinList = []
    #check every single element, when lower than 9. perform recursive function and overwrite number with 10 and increase basin size
    for i in range(height):
        for j in range(width):
            if matrix[i][j] < 9:
                intBasinSize = 1
                matrix[i][j] = 10
                #check up
                if i - 1 >= 0: #check out of bounds
                    intBasinSize += findAdjecent(matrix,i-1,j)
                #check left
                if j - 1 >= 0: #check out of bounds
                    intBasinSize += findAdjecent(matrix,i,j-1)
                #check right
                if j + 1 < width: #check out of bounds
                    intBasinSize += findAdjecent(matrix,i,j+1)
                #check down
                if i + 1 < height: #check out of bounds
                    intBasinSize += findAdjecent(matrix,i+1,j)
                basinList.append(intBasinSize)
    basinList = sorted(basinList,reverse=True)    
    return basinList[0]*basinList[1]*basinList[2]

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print(solvep2("9/input.txt"))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))