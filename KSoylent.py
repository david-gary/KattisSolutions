import math
lines = int(input())
for i in range(lines):
    calories = int(input())
    print(math.ceil(calories/400))