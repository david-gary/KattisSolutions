import sys
def leftshift(numbers):
    n = []
    board = []
    for i in numbers:
        if i != 0:
            n.append(i)
    i = 0
    while i < len(n):
        if i < len(n)-1 and n[i] == n[i+1]:
            board.append(n[i]*2)
            i += 2
        else:
            board.append(n[i])
            i += 1
    while len(board) != 4:
        board.append(0)
    return board

def rightShift(numbers):
    numbers.reverse()
    n = []
    board = []
    for i in numbers:
        if i != 0:
            n.append(i)
    i = 0
    while i < len(n):
        if i < len(n)-1 and n[i] == n[i+1]:
            board.append(n[i]*2)
            i += 2
        else:
            board.append(n[i])
            i += 1
    while len(board) != 4:
        board.append(0)
    board.reverse()
    return board

def shift(numbers):
    board = [[],[],[],[]]
    i = len(numbers[0]) -1
    k = 0
    while i != -1:
        j = 0
        while j < len(numbers):
            board[k].append(numbers[j][i])
            j += 1
        k += 1
        i -= 1
    return board

numbers = []
i = 0
while i < 4:
    numbers.append(list(map(int, sys.stdin.readline().strip().split())))
    i += 1

board = []
direction = sys.stdin.readline().strip()
if direction == "0":
    for line in numbers:
        board.append(leftshift(line))
elif direction == "2":
    for line in numbers:
        board.append(rightShift(line))
elif direction == "1":
    numbers = shift(numbers)
    for line in numbers:
        board.append(leftshift(line))
    board = shift(board)
    board = shift(board)
    board = shift(board)
else:
    numbers = shift(numbers)
    for line in numbers:
        board.append(rightShift(line))
    board = shift(board)
    board = shift(board)
    board = shift(board)

for line in board:
    line = list(map(str, line))
    print(" ".join(line))