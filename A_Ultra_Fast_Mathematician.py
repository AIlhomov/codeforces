s1 = input()
s2 = input()    

value1 = int(s1, 2)
value2 = int(s2, 2)
n = value1 ^ value2
res = ''
while n > 0:
    res = str(n & 1) + res
    n >>= 1
zerosNeeded = len(s1) - len(res) 

print('0' * zerosNeeded + res)
#print(s1 ^ s2)