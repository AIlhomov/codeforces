n, c = map(int, input().split())
p = list(map(int, input().split()))
t = list(map(int, input().split()))

time = 0
Limak = 0
Radewoosh = 0

for i in range(n):
    time += t[i]

    Limak += max(0, p[i] - (c * time))

t.reverse()
p.reverse()
time = 0
for i in range(n):
    time += t[i]
    
    Radewoosh += max(0, p[i] - (c * time))


if Limak == Radewoosh:
    print("Tie")
elif Limak > Radewoosh:
    print("Limak")
else:
    print("Radewoosh")