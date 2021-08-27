i = 0
while True:
    zoos = int(input())
    if zoos == 0:
        break
    i += 1
    print(f"List {i}:")
    animals = {}
    for _ in range(zoos):
        ani = input().split()[-1].lower()
        if ani not in animals:
            animals[ani] = 0
        animals[ani] += 1
    for k in sorted(animals.keys()):
        print(f"{k} | {animals[k]}")
