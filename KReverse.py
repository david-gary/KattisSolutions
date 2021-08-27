lines = int(input())
ogList = ""
for i in range(lines):
    ogList += str(input())
    ogList += str(" ")
ogList = ogList[::-1]
for i in ogList.split():
    print(i[::-1])