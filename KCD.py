while True:
    a, b = map(int, input().split())
    if (a, b) == (0, 0):
        break
    jack = set()
    jill = set()
    for i in range(a):
        jack.add(input())
    for i in range(b):
        jill.add(input())
    cds = jack&jill
    print(len(cds))