n, k = map(int, input().split())
ratings = 0
for i in range(k):
    rating = int(input())
    ratings += rating

minimum = ((n-k)*(-3) + ratings)/n
maximum = ((n-k)*(3)+ratings)/n

print(f"{minimum} {maximum}")
