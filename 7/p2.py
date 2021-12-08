from time import time
from collections import defaultdict

def solvep2(path):
    with open(path) as f:
        lines = f.readlines()
    grid = defaultdict(int)
    maxValue = 0
    total = 0 #to calc avg
    count = 0
    for nr in lines[0].split(','):
        grid[int(nr)] += 1
        total += int(nr)
        count += 1
        if int(nr) > maxValue:
            maxValue = int(nr)
    avg = round(total / count)

    TotalFuel = 0
    lowestTotalFuel = -1
    for i in range(avg-1,avg+1): #to be sure
        for key,value in grid.items():
            _X = int(abs(key - i)) # only positive numbers come from this, so bitshifting is allowed
            _CrabFuel = (_X * (_X+1)) >>1 #Crablogic (fix up2,bitshift instead of fraction to prevent Python from using floats)
            for j in range(value):
                TotalFuel += _CrabFuel
        if TotalFuel < lowestTotalFuel or lowestTotalFuel == -1:
            lowestTotalFuel = TotalFuel
        TotalFuel = 0
    return lowestTotalFuel

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print(solvep2("7/up3.txt"))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))