e, f, c = map(int, input().split())
empty = e + f
total = 0
while empty >= c:
    total += 1
    empty -= (c-1)
print(total)