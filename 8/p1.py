from time import time
from collections import defaultdict
def solvep1(path):
    with open(path) as f:
        lines = f.readlines()
    lstLIST = []
    for line in lines:
        lstLIST.append(line.split(" | ")[1])
    listWords = []
    easyWordCount = 0
    for line in lstLIST:
        for word in line.split(" "):
            word = word.replace('\n',"")
            if len(word) == 2:
                easyWordCount += 1
            if len(word) == 4:
                easyWordCount += 1
            if len(word) == 3:
                easyWordCount += 1
            if len(word) == 7:
                easyWordCount += 1
    return easyWordCount

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print(solvep1("8/input.txt"))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))