n = int(input())
grid = []
for i in range(n):
    grid.append(input().split())

res = 0

# diagonal: 0 0, 1 1, 2 2
# diagonal2: 2 0, 1 1, 0 2

#second diagonal: 1 0, 3 2
#second diagonal2: 0 1, 2 3

for i in range(n):
    for j in range(n):
        # here the center is counted twice probably
        if i == j: #diagonal
            res += int(grid[i][j])
        elif i + j == n - 1:
            res += int(grid[i][j])
        elif i == n // 2:
            res += int(grid[i][j])
        elif j == n // 2:
            res += int(grid[i][j])
print(res)