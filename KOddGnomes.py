lines = int(input())
for i in range(lines):
    total = [int(x) for x in input().split()]
    first = total[0]
    allbutOne = total[1:]
    king = 0
    for i in range(1, first - 1):
        prev = allbutOne[i-1]
        current = allbutOne[i]
        if current - prev != 1:
            king = current
            break
    print(allbutOne.index(king) + 1)