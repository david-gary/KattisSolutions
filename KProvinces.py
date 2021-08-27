from collections import OrderedDict
victory, treasure = OrderedDict(), OrderedDict()
victory = {"Province": 8, "Duchy": 5, "Estate": 2}
treasure = {"Gold": 6, "Silver": 3, "Copper": 0}
inp = list(map(int, input().split()))
money = (inp[0]*3) + (inp[1]*2) + inp[2]
options = []
for coin, cost in treasure.items():
    if money >= cost:
        options.append(coin)
        break
for dominion, cost in victory.items():
    if money >= cost:
        options.insert(0, dominion)
        break

if len(options) == 2:
    print(options[0], "or", options[1])
else:
    print(options[0])