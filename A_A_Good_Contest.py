for i in range(int(input())):
    name, before, after = map(str, input().split())
    before = int(before)
    after = int(after)
    if before >= 2400 and after > before: # and red rated
        print("YES")
        break
else:
    print("NO")