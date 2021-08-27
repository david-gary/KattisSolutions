lines = int(input())
foodTime = set()
for i in range(lines):
    food = list(map(lambda x: int(x), input().split()))
    foodTime.update(range(food[0], 1+food[1]))
print(len(foodTime))