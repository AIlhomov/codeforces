t = int(input())

for i in range(t):
    n = int(input())

    res = 0

    while n != 1:
        if res > 100:
            res = -1
            break
        if n % 6 == 0:
            n //= 6
        else:
            n *= 2
        res += 1
    print(res)