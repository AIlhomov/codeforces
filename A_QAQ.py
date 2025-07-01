s = input()

res = 0

for i in range(len(s)):
    for j in range(i, len(s)):
        for k in range(j, len(s)):
            if s[i] == 'Q' and s[j] == 'A' and s[k] == 'Q':
                res += 1
print(res)