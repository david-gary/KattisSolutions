coins = []
test_cases_no = int(input())
while test_cases_no > 0:
    table = [10001] * 19999 # 19999 = max price - 1 + max coin
    table[0] = 0
    price = int(input())
    coins_no = int(input())
    for i in range(coins_no):
        coins.append(int(input()))
    for coin in coins:
        crt_price = price - 1
        while crt_price >= 0:
            if table[crt_price] == 10001:
                crt_price -= 1
                continue
            if table[crt_price + coin] > table[crt_price] + 1:
                table[crt_price + coin] = table[crt_price] + 1
        crt_price -= 1
    i = price
    while True:
        if table[i] != 10001:
            break
        i += 1
    print(i, table[i])
    test_cases_no -= 1
    coins = []