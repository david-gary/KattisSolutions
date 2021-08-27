lines, width, height = map(int, input().split())
hyp = (((width**2)+(height**2))**0.5)
for x in range(lines):
    i = int(input())
    if i > hyp:
        print("NE")
    else:
        print("DA")