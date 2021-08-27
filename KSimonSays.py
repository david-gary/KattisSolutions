lines = int(input())
for i in range(lines):
    command = input()
    if command[0:10] == 'Simon says':
        print(command[10:])
