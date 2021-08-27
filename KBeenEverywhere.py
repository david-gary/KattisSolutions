lines = int(input())
for i in range(lines):
    total = []
    cities = int(input())
    for x in range(cities):
        check = input()
        if check not in total:
            total.append(check)
    print(len(total))