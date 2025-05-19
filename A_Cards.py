n = int(input())
a = list(map(int, input().split()))

cards = list(enumerate(a, 1))
cards.sort(key=lambda x: x[1])

for i in range(n // 2):
    l = cards[i][0]
    r = cards[n - 1 - i][0]
    print(l, r)