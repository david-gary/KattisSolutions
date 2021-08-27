lines = int(input())
for i in range(lines):
    n = int(input())
    k = 0
    while n > 0:
        k += 0.5
        k *= 2
        n -= 1
    print(int(k))