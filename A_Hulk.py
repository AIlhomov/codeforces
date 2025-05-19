n = int(input())

if n == 1:
    print("I hate it")
elif n == 2:
    print("I hate that I love it")
else:
    #print("I hate that", end=' ')
    for i in range(n-1):
        if i % 2 == 1:
            print("I love that", end=' ')
        else:
            print("I hate that", end=' ')
    if n % 2 == 1:
        print("I hate it")
    else:
        print("I love it")