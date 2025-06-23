red, blue = map(int, input().split())
res = min(red, blue)
c = max(red, blue)
tot = red + blue
print(res, (c - res) // 2)