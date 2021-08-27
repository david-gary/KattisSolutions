import math
lines = int(input())
for i in range(lines):
    x = int(input())
    y = math.factorial(x)
    z = str(y)
    print(z[-1])
    