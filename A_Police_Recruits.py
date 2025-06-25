input()
events = list(map(int, input().split()))
nrOfPolices = 0
res = 0
# -1 = crime
# > 0 = nr of police recruited

for i in range(len(events)):
    if events[i] >= 0:
        nrOfPolices += events[i]
    elif events[i] == -1: # crime occurred
        if nrOfPolices > 0:
            nrOfPolices -= 1
        else:
            res += 1
print(res)