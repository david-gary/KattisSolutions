batters = int(input())
atbats = input().split()
atbatsTotal = 0
for i in atbats:
    print(i)
    atbatsTotal += int(i)
score = (atbats.count('-1')+atbatsTotal)/(batters-atbats.count('-1'))
print(score)