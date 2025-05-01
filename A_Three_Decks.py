t = int(input())


while t > 0:
    
    a, b, c = map(int, input().split())

    sumAll = a + b + c

    diff = b - a

    # if (c - diff) == a+diff and (c - diff) == b:
    #     print("YES")
    # elif (a + b + c) % 3 == 0 and (a + b) < c:
    #     print("YES")
    # # elif c > a + b:
    # #     for i in range(c-(a+b)):
    # #         c -= 1
    # #         minOfthem = 0
    # #         if a > b:
    # #             minOfthem = b
    # #             b += 1
    # #         elif a < b:
    # #             minOfthem = a
    # #             a += 1
    # #         #print(minOfthem, c)
    # #         if a == b:
    # #             print("YES")
    # else:
    #     print("NO")


    c -= diff
    #print(c)
    
    if c >= b: #odd
        minAorB = min(a, b)
        minAorB += diff
        #print(minAorB, c)
        # if minAorB == c:
        #print((c - minAorB) % 3)
        if ((c - minAorB) % 3) == 0:

            print("YES")
        else:
            print("NO")
            
    else:
        print("NO")

    t -= 1