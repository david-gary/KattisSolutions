seq = input()
t = int(seq.count("T"))
c = int(seq.count("C"))
g = int(seq.count("G"))
if t >= 1 and c >= 1 and g >= 1:
    yes = min(t, c, g)
    print((t**2)+(c**2)+(g**2)+(yes*7))
else:
    print((t**2)+(c**2)+(g**2))