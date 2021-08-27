useless = input()
costs = list(map(int, input().split()))
total = 0
for i in costs:
    if i < 0:
        total += (i*(-1))
print(total)