line = str(input())
lower = 0
upper = 0
white = 0
symbol = 0
total = len(line)
for char in line:
    val = ord(char)
    if val == 95:
        white += 1
    elif val in range(65, 91):
        upper += 1
    elif val in range(97, 123):
        lower += 1
    else:
        symbol += 1
print(white/total)
print(lower/total)
print(upper/total)
print(symbol/total)