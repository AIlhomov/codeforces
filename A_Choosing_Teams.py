n, k = map(int, input().split())
y = list(map(int, input().split()))

res = 0
counter = 0 #the teams counter should be 3 to be OK

for i in range(len(y)):
    
    if y[i] + k > 5:
        pass
    else:
        counter += 1
    if counter == 3:
        res += 1
        counter = 0

print(res)