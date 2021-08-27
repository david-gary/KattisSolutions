total = ""
line = 0
for i in range(5):
    line += 1
    inp = input()
    if "FBI" in inp and total == "":
        total += (str(line))
    elif "FBI" in inp and total != "":
        total += (" "+(str(line)))
if total == "":
    print("HE GOT AWAY!")
else:
    print(total)