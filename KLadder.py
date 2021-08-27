import math
h, v = map(float, input().split())
rads = math.radians(v)
out = math.ceil(h/(math.sin(rads)))
print(out)