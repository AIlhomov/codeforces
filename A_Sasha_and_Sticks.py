n, k = map(int, input().split())

moves = n // k

if moves % 2 == 1:
    print("YES")
else:
    print("NO")