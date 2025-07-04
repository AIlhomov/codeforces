x1, x2, x3, x4 = map(int, input().split())

l = sorted([x1, x2, x3, x4])

res1 = l[3] - l[0]
res2 = l[3] - l[1]
res3 = l[3] - l[2]

print(res1, res2, res3)