hand = sorted(input().split())
new = []
for i in hand:
    new.append(i[0])
out = max(set(new), key = new.count)
print(new.count(str(out)))

