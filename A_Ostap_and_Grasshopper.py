n, k = map(int,input().split())
s = input() 
targetIndex = 0
grassHopperIndex = 0
for i in range(n):
    #find the target
    if s[i] == 'G':
        #found the grass hopper (save index)
        grassHopperIndex = i
    elif s[i] == 'T':
        targetIndex = i
#print(grassHopperIndex, targetIndex)
i = grassHopperIndex
dontPrint = False
#right first
while i < n:
    if s[i] == '#':
        break
    elif s[i] == 'T':
        print("YES")
        dontPrint = True
        break
    i += k
#left then
i = grassHopperIndex # reset
while i >= 0:
    if s[i] == '#':
        break
    elif s[i] == 'T':
        print("YES")
        dontPrint = True
        break
    i -= k
if not dontPrint:
    print("NO")