a, b, c = sorted(input().split())
out = ''
order = input()
for i in order:
    if len(out) >= 1:
        out += " "
    if i.lower() == 'c':
        out += str(c)
    if i.lower() == 'a':
        out += str(a)
    if i.lower() == 'b':
        out += str(b)
print(out)