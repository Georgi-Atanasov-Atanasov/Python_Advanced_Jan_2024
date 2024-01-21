rows, columns = [int(el) for el in input().split(", ")]

matrix = []
for _ in range(rows):
    row_nums = [int(el) for el in input().split()]
    matrix.append(row_nums)

for column_index in range(columns):
    column_total = 0
    for row_index in range(rows):
        column_total += matrix[row_index][column_index]
    print(column_total)