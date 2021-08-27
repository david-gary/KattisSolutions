import math
# Faster function to find if a number is prime, using some fundamentals from Number Theory


def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if (n > 2) and (n % 2 == 0):
        return False
    else:
        g = math.floor(math.sqrt(n))
        for i in range(3, (g+1), 2):

            if n % i == 0:
                return False
        return True


sumsList = []


def happy(n):
    return None


lines = int(input())
for i in range(lines):
    line, n = map(int, input().split())
