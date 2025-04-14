n = int(input()) # number of tram stops

people = 0
capacity = 0

for i in range(n):
    a, b = map(int, input().split())
    # a is the amount that exits the tram and b is the amount that enters.
    people -= a
    people += b
    capacity = max(capacity, people)

print(capacity)