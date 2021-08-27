import sys
import math

n,k,q = map(float, input().split())
for i in range(int(q)):
    x, y = map(int, input().split())
    steps = 0
    if x < y:
        x,y = (x-1, y-1)
    else:
        x, y = (y-1, x-1)
    while(x != y):
        y = math.ceil(y/k) - 1
        if x < y:
            x,y = (x,y)
        else:
            x, y = (y,x)
        steps +=1
    print(steps)