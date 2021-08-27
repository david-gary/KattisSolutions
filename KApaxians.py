import sys
inp = str(sys.stdin.readline())
out= ""
for i in range(len(inp)-1):
    if inp [i] != inp[i+1]:
        out += inp[i]
print(out)