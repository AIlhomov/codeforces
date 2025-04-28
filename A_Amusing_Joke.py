guest = input()
host = input()
pile = sorted(input())

if sorted(guest + host) == pile:
    print("YES")
else:
    print("NO")