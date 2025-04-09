def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

t = int(input())
for _ in range(t):
    x, k = map(int, input().split())
    new_num = int(str(x) * k)  # Generate the number y by repeating x k times

    if k == 1:
        if is_prime(x):
            print("YES")
        else:
            print("NO")
    elif k == 2:
        if is_prime(new_num):
            print("YES")
        else:
            print("NO")
    elif k >= 3:
        print("NO")