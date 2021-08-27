companies, requests = map(int, input().split())
OG = list(map(int, input().split()))
for i in range(requests):
    a, b, c = map(int, input().split())
    if a == 1:
        OG[b-1] = c
    else:
        print(abs(b-c))

