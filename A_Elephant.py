x = int(input())
ans = 0
if x % 5 >= 1:
    ans += 1
ans += x // 5
print(ans)