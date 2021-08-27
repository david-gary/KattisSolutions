lines = int(input())
quality = 0.0
for i in range(lines):
    q, y = map(float, input().split())
    quality += (q*y)
print(quality)