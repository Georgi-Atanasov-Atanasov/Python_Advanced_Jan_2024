rows, columns = [int(el) for el in input().split()]
matrix = [[int(el) for el in input().split()] for _ in range(rows)]

current_matrix_sum = float("-inf")
biggest_matrix = []

for row in range(rows - 2):
    for column in range(columns - 2):
        first_row = matrix[row][column:column + 3]
        second_row = matrix[row + 1][column:column + 3]
        third_row = matrix[row + 2][column:column + 3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if current_sum > current_matrix_sum:
            current_matrix_sum = current_sum
            biggest_matrix = [first_row, second_row, third_row]
print(f"Sum = {current_matrix_sum}")
[print(*row) for row in biggest_matrix]
