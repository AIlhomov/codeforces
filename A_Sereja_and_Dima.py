n = int(input())
cards = list(map(int, input().split()))

sereja = 0
dima = 0

turn = 0

while len(cards) != 0:
    n -= 1

    if cards[0] > cards[n]:
        if turn % 2 == 0: #even means its sereja turn
            sereja += cards[0]
        else:
            dima += cards[0]
        cards.pop(0)
    else:
        if turn % 2 == 0: #even means its sereja turn
            sereja += cards[n]
        else:
            dima += cards[n]
        cards.pop()
    turn += 1
print(sereja, dima)