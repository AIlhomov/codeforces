n, c = map(int, input().split())

t = list(map(int, input().split()))
res = 0
for i in range(len(t)-1):
    if t[i+1] - t[i] > c:
        res = 0
    else:
        res += 1
print(res+1)