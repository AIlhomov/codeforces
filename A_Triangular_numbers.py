n = int(input())

flag = False

for i in range(1, n+1):
    if ((i * (i + 1)) / 2 == n):
        print("YES")
        flag = True
        break
if not flag:
    print("NO")
#print((n * (n + 1)) // 2)