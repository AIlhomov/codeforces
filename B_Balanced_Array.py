t = int(input())

def solve(n):

    l = []
    res = []

    for i in range(1,n+1):
        l.append(i)
    
    for i in range(len(l)):
        if l[i] % 2 == 0: # even
            res.append(l[i])
    for i in range(len(l)):
        if l[i] % 2 == 1: #odd
            res.append(l[i])

    addThis = n // 2
    ans = ' '.join(str(x) for x in res[0:len(l)-1])
    print(ans, res[len(l)-1]+addThis)


    #print(res)

while t > 0:

    n = int(input())
    if n % 4 != 0 or n < 4:
        print("NO")
    else:
        print("YES")

        solve(n)


    t -= 1
