lemons, apples, pears = int(input()), int(input()), int(input())
storeI = 0
for i in range(1, lemons+1):
    if i * 2 > apples or i * 4 > pears:
        break
    storeI = i
    

print(storeI + (storeI * 2) + (storeI * 4))