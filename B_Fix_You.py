t = int(input())

for i in range(t):
    n, m = map(int, input().split()) #counter 

    grid = []

    for j in range(n):
        grid.append(input())

    res = 0

    for i in range(n - 1):
        if grid[i][m - 1] != 'D':
            res += 1
    for j in range(m - 1):
        if grid[n - 1][j] != 'R':
            res += 1

    print(res)