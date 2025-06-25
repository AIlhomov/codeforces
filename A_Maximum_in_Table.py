n = int(input())

prev = [1] * n

for i in range(n-1):
    #newTable = []
    summedSoLong = 0
    for j in range(n):
        #prev[i] = first[i]
        summedSoLong += prev[j]
        prev[j] = summedSoLong
    #print(prev)
print(prev[n-1])