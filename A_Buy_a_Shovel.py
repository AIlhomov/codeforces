k, r = map(int, input().split())
allBuys = []
for i in range(1, 100):
    if (i * k) % 10 == 0 or ((i * k) + r) % 10 == 0:
        allBuys.append(i)

print(100 - max(allBuys))