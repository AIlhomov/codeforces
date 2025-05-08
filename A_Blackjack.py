n = int(input())

queen = 10

cardsLeft = n - queen

if cardsLeft == 10:
    print(15)
elif 1 <= cardsLeft <= 11:
    print(4)
else:
    print(0)