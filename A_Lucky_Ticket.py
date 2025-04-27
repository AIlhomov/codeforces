n = int(input())
s = input()

def is_lucky(s):
    lucky = True
    for i in range(len(s)):
        if s[i] not in (7, 4):
            lucky = False
            break
    return lucky

firstHalf = list(map(int, s[0:n//2]))
secondHalf = list(map(int, s[n//2:n]))

if sum(firstHalf) == sum(secondHalf) and is_lucky(firstHalf) and is_lucky(secondHalf):
    print("YES")
else:
    print("NO")