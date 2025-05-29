n, x = map(int, input().split())

distressed_kid = 0

for i in range(n):

    action, amount = map(str, input().split())
    amount = int(amount)
    if action == '+':
        x += amount
    else:
        if x - amount >= 0:
            x -= amount
        else:
            distressed_kid += 1

print(x, distressed_kid)