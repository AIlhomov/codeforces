def maxDiff(a):
    vmin = a[0]
    dmax = 0
    for i in range(len(a)):
        if (a[i] < vmin):
            vmin = a[i]
        elif (a[i] - vmin > dmax):
            dmax = a[i] - vmin
    return dmax

x1, x2, x3 = map(int, input().split())
l = [x1, x2, x3]
l.sort()
print(maxDiff(l))