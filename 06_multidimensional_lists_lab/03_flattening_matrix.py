number_of_matrix_rows = int(input())

flattened_matrix = []

for row in range(number_of_matrix_rows):
    data = [int(el) for el in input().split(", ")]
    flattened_matrix.extend(data)
print(flattened_matrix)