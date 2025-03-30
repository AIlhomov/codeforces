def findX(lower, upper):
    for m in range(1, lower+1):
        x = upper // (m + 1)
        if x * m >= lower:
            #return 'input:%d,%d => %d, obtained with X=%d, Y=%d' % (lower, upper, x, x * m, x * (m+1))
            return x
t = int(input())

#d = nr of grass to each sheep (n)
# Kamilka must choose 2 sheeps x, y 
# which the ans will then be gcd(x,y)

diff_gcd = {}

for i in range(t):
    n = int(input())
    sheeps = list(map(int, input().split()))
    
    print(max(sheeps) - min(sheeps))

    #for j in range(10):
        #diff_gcd[i] = findX(min(sheeps)+j, max(sheeps)+j)
        #print(findX(min(sheeps)+j, max(sheeps)+j))
# print(diff_gcd)
# for key, val in diff_gcd.items():
#     print(val)