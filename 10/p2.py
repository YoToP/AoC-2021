import math
from time import time
def solvep2(path):
    with open(path) as f:
        lines = f.readlines()
    lstTotalScoreList = []
    for line in lines:
        line = line.replace('\n', '')
        lastOpen = []
        bCorruptedLine = False
        lastOpen.append('')
        total = 0
        for i in range(len(line)):
            if not bCorruptedLine:
                if line[i] == '[':lastOpen.append(']')
                elif line[i] == '{':lastOpen.append('}')
                elif line[i] == '<':lastOpen.append('>')
                elif line[i] == '(':lastOpen.append(')')
                else: #is a closer
                    if line[i] != lastOpen.pop():bCorruptedLine = True     
        if not bCorruptedLine:
            while len(lastOpen) > 1:
                _NeededCloseChar = lastOpen.pop()
                if _NeededCloseChar == ']':total = total * 5 + 2
                elif _NeededCloseChar == '}':total = total * 5 + 3
                elif _NeededCloseChar == '>':total = total * 5 + 4
                elif _NeededCloseChar == ')':total = total * 5 + 1   
            lstTotalScoreList.append(total)
    lstTotalScoreList.sort()
    return lstTotalScoreList[math.floor(len(lstTotalScoreList)/2)]

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print(solvep2("10/input.txt"))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))