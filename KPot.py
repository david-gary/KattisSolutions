lines = int(input())
out = 0
for i in range(lines):
    num = int(input())
    base = num//10
    power = int(str(num)[len(str(num))-1])
    out += base**power
print(out)