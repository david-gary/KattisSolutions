a, b = map(int, input().split())
if (a, b) != (0, 0):
    if (a+b) == (a*2):
        print(f"Even {a+b}")
    else:
        print(2*(max(a,b)))
else:
    print('Not a moose')