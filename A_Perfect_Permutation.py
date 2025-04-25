n = int(input())

if n % 2 == 1:
    print(-1)
else:
    l = []
    for i in range(1, n+1):
        l.append(i)
    l.reverse()
    print(*l)