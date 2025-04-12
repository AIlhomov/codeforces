n, h = map(int, input().split())

friends = list(map(int, input().split()))

road = 0

for friend in friends:
    if friend > h:
        road += 2
    else:
        road += 1

print(road)