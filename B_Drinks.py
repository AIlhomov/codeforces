n = int(input())

p = list(map(int, input().split()))
tot = 0

for i in range(len(p)):
    tot += p[i]
    
print(tot / n)