rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

diagonal_sum = 0
for row_index in range(rows):
    for column_index in range(rows): # the matrix is square
        if row_index == column_index:
            diagonal_sum += matrix[row_index][column_index]
print(diagonal_sum)