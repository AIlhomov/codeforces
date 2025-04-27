def palindromic_substrings(s):
    if not s:
        return [[]]
    results = []
    for i in range(len(s), 0, -1):
        sub = s[:i]
        if sub == sub[::-1]:
            for rest in palindromic_substrings(s[i:]):
                results.append([sub] + rest)
    return results

all = palindromic_substrings('radar')
print(all)
for i in range(len(all)):
    for j in range(len(all[i])):
        print(all[i][j])