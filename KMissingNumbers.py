lines = int(input())
nums = []
for i in range(lines):
    nums += [int(input())]
high = max(nums)
out = []
for i in range(1, high+1):
    if i not in nums:
        out += [i]
if len(out) == 0:
    print('good job')
else:
    for i in out:
        print(i)