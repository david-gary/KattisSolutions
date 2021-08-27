alphabet = 'abcdefghijklmnopqrstuvwxyz'
lines = int(input())
for i in range(lines):
    inp = input().lower()
    others = ""
    for x in alphabet:
        if x not in inp:
            others += x
    if others == '':
        print('pangram')
    else:
        print(f'missing {others}')