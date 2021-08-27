lines = int(input())
for i in range(lines):
    nums = input().split()
    others = nums[1:]
    total = 0
    for x in others:
        total += int(x)
    average = total/(float(nums[0]))
    above = 0
    for j in others:
        if int(j) > average:
            above += 1
    finalaverage = round((above/int(nums[0]))*100, 3)
    print("{:.3f}%".format(finalaverage))