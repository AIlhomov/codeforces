t = int(input())

while t > 0:

    n = int(input())
    similiar = ""
    binary_s = input()

    for i in range(0, len(binary_s), 2):
        similiar += binary_s[i]
        
    print(similiar)

    t -= 1

