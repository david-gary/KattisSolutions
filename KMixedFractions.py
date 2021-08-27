on = True
output = []
while on:
    a, b = map(int, input().split())
    if a != 0:
        whole = a//b
        numerator = a%b
        print(f'{whole} {numerator} / {b}')
    else:
        break