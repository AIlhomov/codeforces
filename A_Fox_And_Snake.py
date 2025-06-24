n, m = map(int, input().split())

#2 6 10 14 18    (these digits cannot be divided by 4 mod and give 0)
#4 8 12 16 20
flag = True
for i in range(n):
    for j in range(m):
        if i % 2 == 1:
            if j == 0 and (i+1) % 4 == 0: # the beginning
                print('#', end='')
                flag = False
            elif j == m - 1 and flag: # the end
                print('#', end='')    
            else:
                print(".", end='')
        else:
            print('#', end='')
    print()
    flag = True
