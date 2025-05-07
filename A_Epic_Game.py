from math import gcd

a, b, n = map(int, input().split())
#3 5 9
simonOrAnti = 0

while n >= 0:
    
    x = 0
    if simonOrAnti % 2 == 0: #even simon plays
        x = gcd(a, n)
        n -= x
    else: #odd anti simon plays
        x = gcd(b, n)
        n -= x
    
    simonOrAnti += 1

if simonOrAnti % 2 == 0:
    print(0)
else: 
    print(1)