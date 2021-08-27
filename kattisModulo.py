tot = 0
allnums = []
for i in range(10):
    x = (int(input())%42)
    if x not in allnums:
        tot += 1
        allnums.append(x)
if tot == 0:
    tot = 1
print(tot)