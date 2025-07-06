q = int(input())

for i in range(q):
    n = int(input())
    count = 0
    
    while n != 1:

        if n % 2 == 0:
            n //= 2
            count += 1
        elif n % 3 == 0:
            n = (2*n) // 3
            count += 1
        elif n % 5 == 0:
            n = (4*n) // 5
            count += 1
        else:
            count = -1
            break

    print(count)