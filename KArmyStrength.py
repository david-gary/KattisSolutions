N = int(input())
for i in range(N):
    input()
    amounts = list(map(int, input().split()))
    g = list(map(int, input().split()))
    m = list(map(int, input().split()))
    if max(g) >= max(m):
        print('Godzilla')
    else:
        print('MechaGodzilla')