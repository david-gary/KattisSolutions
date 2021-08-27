mgbs = int(input())
months = int(input())
leftover = 0
for i in range(months):
    current = int(input())
    leftover += (mgbs-current)
print(mgbs+leftover)