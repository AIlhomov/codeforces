s = list(map(int, input().split()))
pattern = input()
res = 0
for i in range(len(pattern)):
    #print(pattern[i])
    res += s[int(pattern[i]) - 1]
print(res)