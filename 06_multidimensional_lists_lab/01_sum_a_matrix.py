rows, columns = [int(el) for el in input().split(',')]
matrix = []
total_sum_of_matrix = 0
for row in range(rows):
    row_data = [int(el) for el in input().split(',')]
    total_sum_of_matrix += sum(row_data)
    matrix.append(row_data)
print(total_sum_of_matrix)
print(matrix)
