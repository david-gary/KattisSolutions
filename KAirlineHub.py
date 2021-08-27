airport_list = []
class Airport:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
    def __repr__(self):
        return "%.2f, %.2f" % (self.x, self.y)
while True:
    try:
        n = int(input())
        for i in range(n):
            airport_list.append(Airport([float(x) for x in input().split()]))
    except EOFError:
        break
for i in airport_list:
    print(i)