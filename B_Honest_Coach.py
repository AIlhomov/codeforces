t = int(input())

for i in range(t):
    n = int(input())

    s = list(map(int, input().split()))
    allDiffs = []
    # find the lowest diff.
    for j in range(len(s)):
        for k in range(len(s)-1, 0, -1):
            if j == k:
                continue
            allDiffs.append(abs(s[j] - s[k]))
    print(min(allDiffs))