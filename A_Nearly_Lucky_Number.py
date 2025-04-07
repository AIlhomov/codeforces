s = input()

s1 = s.count('7')
s2 = s.count('4')
s3 = s1+s2

if s3 == 4 or s3 == 7:
    print("YES")
else:
    print("NO")