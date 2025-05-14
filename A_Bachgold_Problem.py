n = int(input())

if n % 2 == 0:
    #even
    l = [2] * (n // 2)
    print(n // 2)
    print(*l)
else:
    l = [2] * (n // 2 - 1)
    print(n // 2)
    print(*l, 3)