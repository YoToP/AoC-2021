from time import time
def solvep1(path):
    with open(path) as f:
        lines = f.readlines()
    total = 0
    for line in lines:
        line = line.replace('\n', '')
        lastOpen = []
        bCorruptedLine = False
        lastOpen.append('')
        for i in range(len(line)):
            if not bCorruptedLine:
                if line[i] == '[':lastOpen.append(']')
                elif line[i] == '{':lastOpen.append('}')
                elif line[i] == '<':lastOpen.append('>')
                elif line[i] == '(':lastOpen.append(')')
                else: #is a closer
                    if line[i] != lastOpen.pop():
                        if line[i] == ']':total += 57
                        elif line[i] == '}':total += 1197
                        elif line[i] == '>':total += 25137
                        elif line[i] == ')':total += 3   
                        bCorruptedLine = True               
    return total

if __name__ == '__main__': # Run when this script is not imported by another script(e.g. Unittest)
    start_time = int(round(time() * 1000))
    print(solvep1("10/input.txt"))
    print("### total run time is %s miliseconds" % (int(round(time() * 1000)) - start_time))