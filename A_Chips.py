n, m = map(int, input().split())

give = 1

while give <= m:
    
    m -= give
    give += 1
    if give == n+1:
        give = 1
print(m)