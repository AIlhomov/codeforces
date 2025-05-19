n = int(input())

bus = []

for i in range(n):
    bus.append(input())

dontPrint = False
for i in range(n):
    if bus[i][:2] == 'OO':
        bus[i] = '++' + bus[i][2:]
        break
    elif bus[i][3:] == 'OO':
        bus[i] = bus[i][:3] + '++'
        break
else:
    print("NO")
    dontPrint = True
if not dontPrint:
    print("YES")
    print(' \n'.join(bus))
