n, m = map(int, input().split())

checkAll = set()
checkAgainstThis = [i for i in range(1, m+1)]

for i in range(n):
    x = list(map(int, input().split()))

    for i in range(1, len(x)):
        checkAll.add(x[i])
    
if set(checkAgainstThis) == checkAll:
    print("YES")
else:
    print("NO")