hours, minutes = map(int, input().split())
if minutes > 45:
    print(hours, minutes-45)
else:
    if hours != 0 :
        hours -= 1
        minutes += 15
        print(hours, minutes)
    else:
        minutes += 15
        print(f"23 {minutes}")