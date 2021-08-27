lines = int(input())
x = 0
for i in range(lines):
    index, a, b = map(int, input().split())
    c = b - (a**2)
    answer = c**0.5
    print(f"{index} {answer}")

