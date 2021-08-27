windex = 0
highScore = 0
for i in range (1, 6):
    grades = [int(x) for x in input().split()]
    score = sum(grades)
    if score > highScore:
        windex = i
        highScore = score
print(windex, highScore)