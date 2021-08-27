while True:
    sweet, sour = map(int, input().split())
    if (sweet, sour) == (0, 0):
        break
    else:
        if sweet+sour == 13:
            print('Never speak again.')
        else:
            if sweet > sour:
                print("To the convention.")
            elif sour > sweet:
                print("Left beehind.")
            else:
                print("Undecided")