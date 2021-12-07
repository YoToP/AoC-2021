from time import time
from collections import defaultdict
def calcTotal(steps):
    if steps == 0:
        return 0
    total = 1
    for i in range(2,steps+1):
        total += i
    return total


def solvep2(path):
    with open(path) as f:
        lines = f.readlines()
    grid = defaultdict(int)
    maxValue = 0
    for nr in lines[0].split(','):
        grid[int(nr)] += 1
        if int(nr) > maxValue:
            maxValue = int(nr)
    sortedDict=dict(sorted(grid.items(),key= lambda x:x[1],reverse=True))

    TotalFuel = 0
    lowestTotalFuel = 10000000000
    for i in range(maxValue):
        for key,value in grid.items():
            TotalFuel += (calcTotal(abs(key - i))) * value
        if TotalFuel < lowestTotalFuel:
            lowestTotalFuel = TotalFuel
        TotalFuel = 0

    return lowestTotalFuel

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print(solvep2("7/input.txt"))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))