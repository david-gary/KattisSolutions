lines = int(input())
total = 0
for i in range(lines):
    color = input().lower()
    if 'pink' in color or 'rose' in color:
        total += 1
if total > 0:
    print(total)
else:
    print('I must watch Star Wars with my daughter')