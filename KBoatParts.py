a, b = input().split()
items = set()
buyDay = 1
for i in range(int(b)):
	items.add(input())
	if len(items) != int(a):
		buyDay += 1
if len(items) != int(a):
	print("paradox avoided")
else:
	print(buyDay)