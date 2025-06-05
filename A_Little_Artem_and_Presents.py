n = int(input())
odd = 1
counter = 0
if n == 1 or n == 2:
    print(1)
else:
    while n > 0:
        if odd % 2 == 0:
            n -= 1  
        else:
            n -= 2
        odd += 1
        counter += 1
    print(counter)