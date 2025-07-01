cards = input()

flipp = ['a', 'e', 'i', 'o', 'u', '1', '3', '5', '7','9']
res = 0

for c in cards:
    if c in flipp:
        res += 1

print(res)