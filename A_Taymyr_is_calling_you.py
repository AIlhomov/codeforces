n, m, z = map(int, input().split())

artists = z // m
countUpWithm = m
countUpWithn = n

if n == 1:
    print(artists)
else:
    res = 0
    while n <= z and m <= z:
        if m == n:
            res += 1
        if n > m:
            m += countUpWithm
        else:
            n += countUpWithn
    print(res)
# if artists % n == 0:
#     print(artists)
# else:
#     print(artists % n)