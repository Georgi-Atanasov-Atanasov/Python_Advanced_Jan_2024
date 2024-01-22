rows, columns = [int(el) for el in input().split()]
matrix = [input().split() for _ in range(rows)]

number_of_square_matrices = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        starting_character = matrix[row][column]

        if starting_character == matrix[row + 1][column] and starting_character == matrix[row][column + 1] and starting_character == matrix[row + 1][column + 1]:
            number_of_square_matrices += 1

print(number_of_square_matrices)