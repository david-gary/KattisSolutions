import sys
inputs = sys.stdin.read().split("\n")[:-1]
for i in range(len(inputs)):
    earth, mars = map(int, inputs[i].split())
    if earth == mars:
        print ("Case " + str(i+1) + ": 0")
    else:
        total = 0
        while earth != mars:
            total += 1
            earth += 1
            mars += 1
            if earth == 365:
                earth = 0
            if mars == 687:
                mars = 0
        print (f"Case {i+1}: {total}")