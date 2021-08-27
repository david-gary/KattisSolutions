cards = input()
repeats = []
for i in cards:
    if cards.count(i) > 1:
        repeats.append(i)
if len(repeats) > 0:
    print(0)
else:
    print(1)
