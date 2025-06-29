n = int(input())

right = 0
left = 0

for i in range(n):
    x, y = map(int, input().split())

    if x > 0:
        right += 1
    else:
        left += 1

if left <= 1 or right <= 1:
    print("Yes")
else:
    print("No")