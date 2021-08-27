num = int(input())
binary = bin(num).replace("0b", "")
decimal = str(binary)[::-1]
print(int(decimal, 2))