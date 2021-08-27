lines = int(input())
for i in range(lines):
    line, numRange = map(int, input().split())
    s1, s2, s3 = 0, 0, 0
    for i in range(1, numRange+1):
        s1 += i
    for i in range(1, 2*(numRange), 2):
        s2 += i
    for i in range(2, 2*(numRange+1), 2):
        s3 += i
    print(line, s1, s2, s3)