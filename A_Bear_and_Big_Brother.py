limak, bob = map(int, input().split())

years = 0

while (True):
    limak *= 3
    bob *= 2
    years += 1
    if (limak > bob):
        break
print(years)