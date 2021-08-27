import math
factorial = int(input())
inverse = (math.log(factorial, 10))
out = str(inverse-1).split('.')
print(out[0])