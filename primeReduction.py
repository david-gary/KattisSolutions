import math
factors = []
process = 1


def isPrime(n, factors, process):
    prime = True
    if n == 2:
        factors.append(2)
        print('2 1')
    if (n > 2) and (n % 2 == 0):
        factors.append(2)
        factors.append(n/2)
        n /= 2
        process += 1
        isPrime(n)
    else:
        g = math.floor(math.sqrt(n))
        for i in range(3, (g+1), 2):
            if n % i == 0:
                factors.append(i)
                prime = False
        if prime:
            print(f'{n}, {process}')
    return factors, process


while True:
    try:
        n = int(input())
        isPrime(n, factors, process)
    except EOFError:
        break
