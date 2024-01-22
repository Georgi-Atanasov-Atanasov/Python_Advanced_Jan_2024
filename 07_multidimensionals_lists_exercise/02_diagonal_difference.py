size_of_the_matrix = int(input())

primary_diagonal_sum, secondary_diagonal_sum = 0, 0

for i in range(size_of_the_matrix):
    matrix_row = [int(x) for x in input().split()]
    primary_diagonal_sum += matrix_row[i]
    secondary_diagonal_sum += matrix_row[size_of_the_matrix - i - 1]

print(abs(primary_diagonal_sum - secondary_diagonal_sum))