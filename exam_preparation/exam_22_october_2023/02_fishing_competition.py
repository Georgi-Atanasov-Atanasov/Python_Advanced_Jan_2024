# def calculate_position(ma, row, column):
#     if row < 0:
#         row = len(ma) - 1
#     if column < 0:
#         column = len(ma) - 1
#     if row >= len(ma):
#         row = 0
#     if column >= len(ma):
#         column = 0
#     return row, column
#
#
# size_of_the_matrix = int(input())
# matrix = []
#
# position = []
# passages = 0
# whirpool = False
#
# directions = {
#     "up": [-1, 0],
#     "down": [1, 0],
#     "left": [0, -1],
#     "right": [0, 1]
# }
#
# for row in range(size_of_the_matrix):
#     matrix.append(input())
#     for column in range(size_of_the_matrix):
#         if matrix[row][column] == "-":
#             continue
#         elif matrix[row][column] == "S":
#             position = row, column
#         elif matrix[row][column] == "W":
#             whirpool = True
#             print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: {position}]")
#             break
#         elif matrix[row][column].isdigit():
#             passages += int(matrix[row][column])
#             matrix[row][column] = "-"
#
#         while 0 <= row < size_of_the_matrix and 0 <= column < size_of_the_matrix or passages < 20:
#             while passages < 20:
#                 command = input()
#                 current_row, current_col = position
#                 if command == "up":
#                     row, col = calculate_position(matrix, current_row - 1, current_col)
#                 elif command == "down":
#                     row, col = calculate_position(matrix, current_row + 1, current_col)
#                 elif command == "right":
#                     row, col = calculate_position(matrix, current_row, current_col + 1)
#                 elif command == "left":
#                     row, col = calculate_position(matrix, current_row, current_col - 1)
#
# if passages >= 20:
#     print("Success! You managed to reach the quota!")
# else:
#     print("You didn't catch enough fish and didn't reach the quota!")
#     print(f"You need {20 - passages} tons of fish more.")
# if 20 > passages > 0:
#     print(f"Amount of fish caught: {passages} tons.")
# if whirpool == False:
#     print(matrix)
#




def correct_position(row, col, size):
    if row < 0:
        row = size - 1
    if row == size:
        row = 0
    if col < 0:
        col = size - 1
    if col == size:
        col = 0
    return row, col


directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "right": [0, 1],
    "left": [0, -1]
}
size = int(input())
fishing_area = [[ch for ch in input()] for _ in range(size)]
my_position = [[row, col] for col in range(size) for row in range(size) if fishing_area[row][col] == "S"][0]
fishing_area[my_position[0]][my_position[1]] = "-"
collected_fishes = 0

command = input()

while command != "collect the nets":
    row = directions[command][0] + my_position[0]
    col = directions[command][1] + my_position[1]
    row, col = correct_position(row, col, size)
    my_position = [row, col]

    if fishing_area[row][col].isdigit():
        collected_fishes += int(fishing_area[row][col])
        fishing_area[row][col] = "-"
    elif fishing_area[row][col] == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{my_position[0]},{my_position[1]}]")
        exit()

    command = input()

fishing_area[my_position[0]][my_position[1]] = "S"
if collected_fishes >= 20:
    print("Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - collected_fishes} tons of fish more.")

if collected_fishes > 0:
    print(f"Amount of fish caught: {collected_fishes} tons.")

for line in fishing_area:
    print(''.join(line))


# Ines version

def get_next_position(position, directions_to_move, matrix):
    current_row_index, current_col_index = position
    row_movement, col_movement = directions_to_move[command]
    desired_row_index = current_row_index + row_movement
    desired_col_index = current_col_index + col_movement

    if 0 <= desired_row_index < len(matrix) and 0 <= desired_col_index < len(matrix):
        return desired_row_index, desired_col_index

    if desired_row_index < 0:
        desired_row_index = len(matrix) - 1
    elif desired_row_index >= len(matrix):
        desired_row_index = 0

    if desired_col_index < 0:
        desired_col_index = len(matrix) - 1
    elif desired_col_index >= len(matrix):
        desired_col_index = 0

    return desired_row_index, desired_col_index



n = int(input())

directions_to_move = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

matrix = []

position = None

for row_index in range(n):
    data = list(input())

    if "S" in data:
        current_col = data.index("S")
        position = [row_index, current_col]
    matrix.append(data)

command = input()
collected_fish = 0

while command != "collect the nets":
    current_row_index, current_col_index = position
    next_row_index, next_col_index = get_next_position(position, directions_to_move, matrix)

    symbol = matrix[next_row_index][next_col_index]
    matrix[next_row_index][next_col_index] = "S"
    matrix[current_row_index][current_col_index] = "-"
    position = [next_row_index, next_col_index]

    if symbol.isdigit():
        collected_fish += int(symbol)
    elif symbol == "W":
        print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{position[0]},{position[1]}]")
        exit()
    command = input()

if collected_fish >= 20:
    print(f"Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - collected_fish} tons of fish more.")


if collected_fish > 0:
    print(f"Amount of fish caught: {collected_fish} tons.")

[print(*row, sep='') for row in matrix]