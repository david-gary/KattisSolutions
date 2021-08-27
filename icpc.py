lines = int(input())
all_teams = []
winners = []
for i in range(lines):
    loc, team = map(str, input().split())
    if loc not in all_teams:
        all_teams.append(loc)
        new = (f"{loc} {team}")
        winners.append(new)
for x in range(12):
    print(winners[x])
