from math import ceil
cases = int(input())
for i in range(cases):
    useless = int(input())
    stores = list(map(int, input().split()))
    x = ceil(sum(stores)/len(stores))
    print((abs(x - min(stores)) + abs(x - max(stores))) * 2)