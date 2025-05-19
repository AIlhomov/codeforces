n = int(input())
Mishka = 0
Chris = 0
for i in range(n):
    m, c = map(int, input().split())
    if m > c:
        Mishka += 1
    elif c > m:
        Chris += 1

if Chris > Mishka:
    print("Chris")
elif Chris < Mishka:
    print("Mishka")
else:
    print("Friendship is magic!^^")