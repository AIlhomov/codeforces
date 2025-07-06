t = int(input())

while t != 0:

    n = int(input()) #nr of gifts
    a = list(map(int, input().split())) #nr of candies in the Ith gift
    b = list(map(int, input().split())) #nr of oranges in the Ith gift

    #find the min in total
    minA = min(a)
    minB = min(b)

    res = 0

    for i in range(len(a)):

        if a[i] > minA and b[i] > minB:
            #eat both
            res += max(a[i] - minA, b[i] - minB)
            #res += a[i] - minA
        else:
            res += a[i] - minA + b[i] - minB
    
    print(res)


    t -= 1