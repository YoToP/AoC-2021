from time import time
from collections import defaultdict
def solvep1(path):
    with open(path) as f:
        lines = f.readlines()
    matrix = []
    for line in lines:
        line = line.replace('\n', '')
        lstLine = []
        for nr in line:
            lstLine.append(int(nr))
        matrix.append(lstLine)
    height = len(matrix)
    width = len(matrix[0])
    pointer = (0,0)
    total = 0
    for i in range(height):
        for j in range(width):
            directionsHigher = 4
            #check up
            if i - 1 >= 0: #check out of bounds
                if matrix[i][j] < matrix[i-1][j]: directionsHigher -= 1
            else: directionsHigher -= 1
            #check left
            if j - 1 >= 0: #check out of bounds
                if matrix[i][j] < matrix[i][j-1]: directionsHigher -= 1
            else: directionsHigher -= 1
            #check right
            if j + 1 < width: #check out of bounds
                if matrix[i][j] < matrix[i][j+1]: directionsHigher -= 1
            else: directionsHigher -= 1
            #check down
            if i + 1 < height: #check out of bounds
                if matrix[i][j] < matrix[i+1][j]: directionsHigher -= 1
            else: directionsHigher -= 1
            if directionsHigher == 0:total += 1+matrix[i][j]
    return total

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print(solvep1("9/input.txt"))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))