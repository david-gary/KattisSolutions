useless = input()
adrian = "A, B, C" * 34
bruno = "B, A, B, C," * 25
gorian = "C, C, A, A, B, B," * 20
test = input()
apoint = 0
bpoint = 0
gpoint = 0
for i in test:
    if bruno[test.index(i)] == test[test.index(i)]:
        bpoint += 1
    if adrian[test.index(i)] == test[test.index(i)]:
        apoint += 1
    if gorian[test.index(i)] == test[test.index(i)]:
        gpoint += 1
high = max(apoint, bpoint, gpoint)
print(high)
if apoint == high:
    print("Adrian")
if bpoint == high:
    print("Bruno")
if gpoint == high:
    print("Goran")