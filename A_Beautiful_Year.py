n = int(input())
n += 1

year = list(str(n))

while len(set(year)) != len(year):
    n += 1
    year = list(str(n))
print(''.join(year))