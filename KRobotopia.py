lines = int(input())
for i in range(lines):
    robot = list(map(int, input().split()))
    leg1, arm1, leg2, arm2, legs, arms = robot[0], robot[1], robot[2], robot[3], robot[4], robot[5]
    output = ''
    answers = 0
    limit = max({legs, arms})
    for x in range(1, limit):
        Lremain = legs - (x * leg1)
        Aremain = arms - (x * arm1)
        if (Lremain > 0) & (Aremain > 0):
            if Aremain % arm2 == 0:
                if Lremain % leg2 == 0:
                    if Aremain * leg2 == Lremain * arm2:
                        answers += 1
                        output = "{} {:g}".format(x, Aremain / arm2)
    if answers == 1:
        print(output)
    else:
        print("?")