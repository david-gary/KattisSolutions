import math
lengths = input()
a,b,c,d = map(int, lengths.split())
s = (a+b+c+d)/2
t = math.sqrt((s-a)*(s-b)*(s-c)*(s-d))
print(t)
