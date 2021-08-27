n, l = map(int, input().split())
time = 0
traveled = 0
for _ in range(n):
    d, r, g = map(int, input().split())
    time += (d - traveled)
    traveled = d
    if time % (r + g) < r:
        time += r - time % (r + g)
print(time + l - traveled)