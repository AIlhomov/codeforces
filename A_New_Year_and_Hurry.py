n, k = map(int, input().split())
# n problems
# k minutes

hours4 = 4*60 # 240 overall time to get there

hours4 -= k
ans = 0

for i in range(1, n+1):
    problem = i * 5
    if problem <= hours4:
        ans += 1
        hours4 -= problem
print(ans)