n = int(input())
s = input() 

black = []
counter = 0

for c in s:
    if c == 'B':
        counter += 1
    elif c == 'W':
        black.append(counter)
        counter = 0
#print(black)
black.append(counter)
res = []
for elem in black:
    if elem != 0:
        res.append(elem)
        
print(len(res))
print(*res)