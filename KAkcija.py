import sys
prices = sorted(sys.stdin.read().split("\n")[1:-1], key=int, reverse=True)
books = ([prices[i:i + 3] for i in range(0, len(prices), 3)])
out = 0
for i in books:
    i = [int(x) for x in i]
    if len(i) == 3:
        out += (sum(i) - min(i))
    else:
        out += sum(i)
print(out)