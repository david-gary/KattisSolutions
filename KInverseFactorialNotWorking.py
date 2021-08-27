def inverseFactorial(num):
    n = 1
    factored = 0
    while True:
        factored += 1
        n = factored*n
        if n >= num:
            break
    return factored
num = int(input())
print(inverseFactorial(num))