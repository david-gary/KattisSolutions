lines = int(input())
players = []
for i in range(lines):
    new = input()
    players.append(new)
if players != sorted(players, reverse=True) and players != sorted(players):
    print("NEITHER")
if players != sorted(players, reverse=True) and players == sorted(players):
    print("INCREASING")
if players == sorted(players, reverse=True) and players != sorted(players):
    print("DECREASING")