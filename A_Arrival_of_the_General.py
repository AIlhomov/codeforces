n = int(input())

heights = list(map(int, input().split()))

findMinIndex = 0
findMaxIndex = 0

maxHeight = heights[0]
minHeight = heights[0]
#max = left
#min = right
for i in range(n):
    if heights[i] > maxHeight: # we use > because we want the closest right
        maxHeight = heights[i]
        findMaxIndex = i
    elif heights[i] <= minHeight: # we use <= because we want the closest left
        minHeight = heights[i]
        findMinIndex = i

#print(findMaxIndex, findMinIndex)

if findMaxIndex > findMinIndex:
    print(findMaxIndex + (n - findMinIndex) - 2 )
else:
    print(findMaxIndex + (n - findMinIndex) - 1 )