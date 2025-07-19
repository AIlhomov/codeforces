t = int(input())

for i in range(t):
    a, b, n = map(int, input().split())

    #find the min
    res = 0

    while a <= n and b <= n:
        if a > b:
            b += a
        else:
            a += b
        res += 1
    print(res)
