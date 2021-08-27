lines = int(input())
for line in range(lines):
    i = int(input())
    if i%2 == 0:
        print(f'{i} is even')
    else:
        print(f'{i} is odd')
