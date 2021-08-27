import math
lines = int(input())
hours = [0]
distances = [0]
for i in range(lines):
    a, b = map(int, input().split())
    hours.append(a)
    distances.append(b)
distdiffHigh = 0
for x in range(len(distances)-1):
    try:
        potNew = ((distances[x+1] - distances[x]))/(hours[x+1] - hours[x]) 
        if potNew > distdiffHigh:
            distdiffHigh = potNew
    except ZeroDivisionError:
        pass
print(math.floor(distdiffHigh))


