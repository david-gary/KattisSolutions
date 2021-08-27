import math
bigBoy = input()
howBig = len(bigBoy)
if howBig < 10:
    factoredA, gitBig, splitBig = 1, 1, int(bigBoy)
    while gitBig < splitBig:
        factoredA += 1
        gitBig *= factoredA
    print(factoredA)
else:
    logCompare, factoredB = 0, 0
    while logCompare < howBig-1:
        factoredB += 1
        logCompare += math.log(factoredB, 10)
    print(factoredB)