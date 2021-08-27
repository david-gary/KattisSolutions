lines = int(input())
for i in range(lines):
    a, b ,c = input().split()
    if (int(a) + int(c)) == int(b):
        print("does not matter")
    elif (int(a) + int(c)) < int(b):
        print('advertise')
    elif (int(a) + int(c)) > int(b):
        print('do not advertise')
    