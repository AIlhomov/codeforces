n, m = map(int, input().split())

res = 0

for a in range(1000):
    for b in range(1000):
        if a * a + b == n and a + b * b == m:
            res += 1
print(res)