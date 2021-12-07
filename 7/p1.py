from time import time
from collections import defaultdict
def solvep1(path):
    with open(path) as f:
        lines = f.readlines()
    lstLIST = []
    grid = defaultdict(int)
    total = 0 #to calc avg
    count = 0
    for nr in lines[0].split(','):
        grid[int(nr)] += 1
        total += int(nr)
        count += 1
    sortedDict=dict(sorted(grid.items(),key= lambda x:x[1],reverse=True))
    avg = total / count

    #HighestAmountKey = -1
    #HighestAmountValue = -1
    #for key,value in sortedDict.items():
    #    if value > HighestAmountValue:
    #        HighestAmountValue = value
    #        HighestAmountKey = key
    
    TotalFuel = 0
    lowestTotalFuel = 1000000
    for SortedKey,SortedValue in sortedDict.items():
        for key,value in grid.items():
            TotalFuel += (abs(key - SortedKey)) * value
        if TotalFuel < lowestTotalFuel:
            lowestTotalFuel = TotalFuel
        TotalFuel = 0

    return lowestTotalFuel

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print(solvep1("7/input.txt"))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))