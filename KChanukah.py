lines = int(input())
candles = 0
steps = 0
for x in range(lines):
    n, k = map(int, input().split())
    for i in range(1, n):
        candles += 1
        k += candles
    steps += 1
    print(f'{steps} {k}')