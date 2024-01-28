size_of_the_matrix = int(input())

matrix = []
bunny_position = []

for row in range(size_of_the_matrix):
    matrix.append(input().split())
    for column in range(size_of_the_matrix):
        if matrix[row][column] == "B":
            bunny_position = [row, column]

possible_directions_to_move = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

max_collected_eggs = float('-inf')
best_direction = ''
best_path = []

for direction, move in possible_directions_to_move.items():
    current_eggs = 0
    current_eggs_matrix = []
    row = bunny_position[0] + move[0] #taking indexes from possible directions(row,column)
    column = bunny_position[1] + move[1]

    while 0 <= row < size_of_the_matrix and 0 <= column < size_of_the_matrix:
        if matrix[row][column] == "X":
            break

        current_eggs += int(matrix[row][column])
        current_eggs_matrix.append([row, column])
        row += move[0]
        column += move[1]

    if current_eggs > max_collected_eggs and current_eggs_matrix:
        max_collected_eggs = current_eggs
        best_direction = direction
        best_path = current_eggs_matrix

print(best_direction)
[print(row) for row in best_path]
print(max_collected_eggs)
