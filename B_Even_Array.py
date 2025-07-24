t = int(input())

for i in range(t):
    n = int(input())

    a = list(map(int, input().split()))

    even = 0 #wrong ones
    odd = 0

    for j in range(len(a)):
        if j % 2 != a[j] % 2:
            if j % 2 == 0:
                even += 1
            else:
                odd += 1
    if even == odd:
        print(even)
    else:
        print(-1)