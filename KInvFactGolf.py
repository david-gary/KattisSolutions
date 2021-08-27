import math
num = int(input())
factorial = 1
for i in range(1, num+1):
    factorial = factorial*i
print(factorial)
inverse = (math.log(factorial, 10))
out = str(inverse-1).split('.')
print(out[0])