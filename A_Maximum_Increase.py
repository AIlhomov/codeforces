n = int(input())
arr = list(map(int, input().split()))
res = 1
m = 1
for i in range(1, n):
    if arr[i] > arr[i-1]:
        res += 1
    else:
        if m < res:
            m = res
        res = 1
    if m < res:
        m = res
print(m)