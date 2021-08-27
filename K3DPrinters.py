statues = int(input())
def printTime(statues):
    time = 0
    printers = 1
    while printers < statues:
        time += 1
        printers *= 2
    time+=1
    return time
print(printTime(statues))