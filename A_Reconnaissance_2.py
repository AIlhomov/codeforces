input()

soldiers = list(map(int, input().split()))

heights = set()

for i in range(len(soldiers)):
    for j in range(len(soldiers)):
        #neighbours and those in the circle neighbours
        if (i-1 == j or j-1 == i) or (i == 0 and j == len(soldiers)-1) or (j == 0 and i == len(soldiers)-1):
            #make a dict of the height and the 2 soldiers index
            key = abs(soldiers[i] - soldiers[j])
            value = (i+1, j+1)
            #append the height and the index of the 2 soldiers
            heights.add((key, value))
        
#find min key in heights set and output the indexes
findMin = min(heights)

print(findMin[1][0], findMin[1][1])
