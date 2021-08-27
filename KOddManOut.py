problems = int(input())
casenumber = 0
for i in range(problems):
    casenumber += 1
    useless = int(input())
    numbers = sorted(input().split())
    for i in numbers:
        if numbers.count(i)%2 != 0:
            print(f'Case #{casenumber}: {i}')
    