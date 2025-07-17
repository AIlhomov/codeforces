from itertools import groupby

t = int(input())

for i in range(t):
    s = input()

    blocks = [len(list(g)) for k, g in groupby(s) if k == '1']
    blocks.sort(reverse=True)

    ans = 0

    for j in range(0, len(blocks), 2):
        ans += blocks[j]
    print(ans)