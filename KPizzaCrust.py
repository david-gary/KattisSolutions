import math
pizza = input().split()
radius = float(pizza[0])
crust = float(pizza[1])
cheese = (radius - crust) ** 2
out = (cheese/(radius**2)) * 100
print(out)