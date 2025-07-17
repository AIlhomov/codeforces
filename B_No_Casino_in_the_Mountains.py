t = int(input())

for i in range(t):
    n, k = map(int, input().split())

    a = list(map(int, input().split()))

    counter = 0
    res = 0
    i = 0

    while i < n:
        if a[i] == 0:
            counter += 1
        else:
            counter = 0
        
        if counter == k:
            res += 1
            counter = 0
            i += 1 #apparently he needs rest.. weakling
        i += 1
    print(res)