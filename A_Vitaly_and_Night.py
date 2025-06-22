n, m = map(int, input().split())
res = 0
for i in range(n):
    floor = list(map(int, input().split()))

    for j in range(0, len(floor), 2):
        if floor[j] == 1 or floor[j+1] == 1:
            res += 1
print(res)