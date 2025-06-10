n = int(input())
cake = []

for i in range(n):
    cake.append(input())

happiness = 0

# rows
for row in cake:
    for i in range(len(row)):
        for j in range(i + 1, len(row)):
            if row[i] == 'C' and row[j] == 'C':
                happiness += 1

# columns
for col in range(len(cake[0])):
    for i in range(len(cake)):
        for j in range(i + 1, len(cake)):
            if cake[i][col] == 'C' and cake[j][col] == 'C':
                happiness += 1

print(happiness)
