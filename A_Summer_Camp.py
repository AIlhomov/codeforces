n = int(input())
digits = ""
for i in range(1, n+1):
    digits += str(i)

print(digits[n-1])