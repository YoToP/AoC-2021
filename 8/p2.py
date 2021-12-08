from time import time
from collections import defaultdict
def solvep2(path):
    with open(path) as f:
        lines = f.readlines()
    lstSegmentLIST = []
    lstOutputLIST = []
    for line in lines:
        words = line.split(" ")
        _output = False
        lstLineSegmentList = []
        lstLineOutputList = []
        for i in range(len(words)):
            if words[i] == "|":
                _output = True
            elif _output:
                lstLineOutputList.append("".join(sorted(words[i])).replace('\n',""))
            else:
                lstLineSegmentList.append("".join(sorted(words[i])))
            lstSegmentLIST.append(lstLineSegmentList)
            lstOutputLIST.append(lstLineOutputList)

    easyWordCount = 0
    for i in range(len(lstOutputLIST)):
        line = lstOutputLIST[i]
        woordenboek = defaultdict(int)
        lstMissingNrs = []
        #1 Determine missing nr

        for word in line:
            if len(word) == 5:
                if not lstMissingNrs.__contains__(word):
                    lstMissingNrs.append(word)
            if len(word) == 6:
                if not lstMissingNrs.__contains__(word):
                    lstMissingNrs.append(word)
        #1.5Add known
        for word in lstSegmentLIST[i]:
            #word = word.replace('\n',"")
            if len(word) == 2:woordenboek[1] = word
            if len(word) == 3:woordenboek[7] = word
            if len(word) == 4:woordenboek[4] = word
            if len(word) == 7:woordenboek[8] = word
        #2 Decipher number
        for word in lstMissingNrs: # only decipher words that are needed
            if len(word) == 5: #could 2,3 or 5
                lettercount  = 0
                bDone = False
                if woordenboek[3] == 0:
                    for letter in woordenboek[7]: #only 7 can completly go into 3
                        if word.find(letter) >= 0:
                            lettercount += 1
                        if lettercount == 3: # all 3 letter of seven must go into 3, or it is not 3
                            woordenboek[3] = word
                            bDone = True
                lettercount = 0
                if woordenboek[5] == 0 and not bDone:
                    for letter in woordenboek[4]: #out of nr2 and nr5,nr5 can hold 3/4 letters of nr4
                        if word.find(letter) >= 0:
                            lettercount += 1
                        if lettercount == 3: # 3/4 can go into nr5
                            woordenboek[5] = word
                            bDone = True
                if woordenboek[2] == 0 and not bDone:
                    woordenboek[2] = word # that is all that is left
            elif len(word) == 6: #could 6,9 or 0
                lettercount = 0
                bDone = False
                if woordenboek[6] == 0:
                    for letter in woordenboek[1]: #only nr6 can hold 1 letter of nr1
                        if word.find(letter) >= 0:lettercount += 1
                    if lettercount == 1: # only nr 6 cannot hold nr1, so if after the loop the total = 1, its nr6
                        woordenboek[6] = word
                        bDone = True
                lettercount = 0
                if woordenboek[9] == 0 and not bDone:
                    for letter in woordenboek[4]: #only nr4 can completly go into nr9
                        if word.find(letter) >= 0:
                            lettercount += 1
                        if lettercount == 4: # all 3 letter of seven must go into 3, or it is not 3
                            woordenboek[9] = word
                            bDone = True
                if woordenboek[0] == 0 and not bDone:woordenboek[0] = word # that is all that is left
        #3 construct outcome
        StringConstruct = ""
        for word in line:
            if len(word) == 2:StringConstruct += "1"
            elif len(word) == 3:StringConstruct += "7"
            elif len(word) == 4:StringConstruct += "4"
            elif len(word) == 5:
                if woordenboek[2] != 0: #if not in woordenboek, then not required to check
                    lettercount = 0
                    for letter in woordenboek[2]:
                        if word.find(letter) >= 0:lettercount += 1
                        if lettercount == 5:StringConstruct += "2"
                if woordenboek[3] != 0: #if not in woordenboek, then not required to check
                    lettercount = 0
                    for letter in woordenboek[3]:
                        if word.find(letter) >= 0:lettercount += 1
                        if lettercount == 5:StringConstruct += "3"
                if woordenboek[5] != 0: #if not in woordenboek, then not required to check
                    lettercount = 0
                    for letter in woordenboek[5]:
                        if word.find(letter) >= 0:lettercount += 1
                        if lettercount == 5:StringConstruct += "5"
            elif len(word) == 6:
                if woordenboek[6] != 0: #if not in woordenboek, then not required to check
                    lettercount = 0
                    for letter in woordenboek[6]:
                        if word.find(letter) >= 0:lettercount += 1
                        if lettercount == 6:StringConstruct += "6"
                if woordenboek[9] != 0: #if not in woordenboek, then not required to check
                    lettercount = 0
                    for letter in woordenboek[9]:
                        if word.find(letter) >= 0:lettercount += 1
                        if lettercount == 6:StringConstruct += "9"
                if woordenboek[0] != 0: #if not in woordenboek, then not required to check
                    lettercount = 0
                    for letter in woordenboek[0]:
                        if word.find(letter) >= 0:lettercount += 1
                        if lettercount == 6:StringConstruct += "0"
            elif len(word) == 7:StringConstruct += "8"
        #4 count to total
        easyWordCount += int(StringConstruct)
    return easyWordCount

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print(solvep2("8/input.txt"))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))