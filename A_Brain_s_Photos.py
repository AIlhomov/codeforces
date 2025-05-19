r, c = map(int, input().split())
matrix = []
for i in range(r):
    matrix.append(input().split(' '))
    if 'C' in matrix[i] or 'M' in matrix[i] or 'Y' in matrix[i]:
        print("#Color")
        break
else:
    print("#Black&White")
#print(matrix)