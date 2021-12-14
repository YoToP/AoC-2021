from time import time
from collections import defaultdict
def solvep1(path,MAX_ITERATIONS):
    with open(path) as f: lines = f.readlines()
    lstPairList = defaultdict(int)
    lstInstructions = []
    bFirstRead = True
    for line in lines: #First run, check for all the starts,end and the rest and seperate them
        line = line.replace('\n', '')
        if bFirstRead:
            for i in range (1,len(line)):
                lstPairList[line[i-1],line[i]] += 1
            bFirstRead = False
        elif len(line)> 0:
            _pair, _toAdd = line.split(" -> ")
            lstInstructions.append((_pair,_toAdd))
    i = 0
    while(i<MAX_ITERATIONS):
        lstOldPairList = lstPairList.copy()
        lstPairList.clear()
        for _instruction in lstInstructions:
            for _tuple, _amount in lstOldPairList.items():
                if _tuple == (_instruction[0][0],_instruction[0][1]): #instruction is same as in list
                    lstPairList[(_instruction[0][0],_instruction[1])] += _amount
                    lstPairList[(_instruction[1],_instruction[0][1])] += _amount
        i += 1

    lstLetterList = defaultdict(int)
    lstLetterList2 = defaultdict(int) #control list
    for _tuple, _amount in lstPairList.items():
        lstLetterList[_tuple[0]] += _amount
        lstLetterList2[_tuple[1]] += _amount
    for _letter, _amount in lstLetterList2.items(): #correct for start/end (off by one)
        if _amount != lstLetterList[_letter]:
            if _amount > lstLetterList[_letter]:
                lstLetterList[_letter] = _amount

    minValue = -1
    maxValue = 0
    for _letter, _amount in lstLetterList.items():
        if _amount > maxValue: maxValue = _amount
        if minValue == -1:
            minValue = _amount
        if _amount < minValue:
            minValue = _amount
    return maxValue - minValue

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print('p1:',solvep1("14/input.txt",10))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))
    start_time = int(round(time() * 1000))
    print('p2:',solvep1("14/input.txt",40))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))