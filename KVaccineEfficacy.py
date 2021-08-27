lines = int(input())
vaccinated = 0
unvaccinated = 0
av, bv, cv = 0, 0, 0
au, bu, cu = 0, 0, 0
for i in range(lines):
    inp = input()
    if inp[0] == 'Y':
        vaccinated += 1
        if inp[1] == 'Y':
            av += 1
        if inp[2] == 'Y':
            bv += 1
        if inp[3] == 'Y':
            cv += 1
    else:
        unvaccinated += 1
        if inp[1] == 'Y':
            au += 1
        if inp[2] == 'Y':
            bu += 1
        if inp[3] == 'Y':
            cu += 1
a = (1-(av/au))*100
if a > 0:
    print("{:.6f}".format(a))
else:
    print('Not Effective')
b = (1-(bv/bu))*100
if b > 0:
    print("{:.6f}".format(b))
else:
    print('Not Effective')
c = (1-(cv/cu))*100
if c > 0:
    print("{:.6f}".format(c))
else:
    print('Not Effective')