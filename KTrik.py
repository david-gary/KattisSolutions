loc = 1
for i in input():
    if i == 'A':
        if loc == 1:
            loc = 2
        elif loc == 2:
            loc = 1
        else:
            loc = 3
    elif i == 'B':
        if loc == 1:
            loc = 1
        elif loc == 2:
            loc = 3
        else:
            loc = 2

    else:
        if loc == 1:
            loc = 3
        elif loc == 2:
            loc = 2
        else:
            loc = 1
print(loc)