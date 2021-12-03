def solvep2(path):
    with open(path) as f:
        lines = f.readlines()
    depth = 0
    hor = 0
    aim = 0
    for line in lines:
        lineElements = line.split(" ")
        if lineElements[0] == "forward":
            hor = hor + int(lineElements[1])
            depth = depth + (aim * int(lineElements[1]))
        elif lineElements[0] == "up":
            aim = aim - int(lineElements[1])
        elif lineElements[0] == "down":
            aim = aim + int(lineElements[1])
    return hor*depth

if __name__ == '__main__':
    print(solvep2("2/input.txt"))