size_of_the_board = int(input())

matrix = []
knights = []

for row in range(size_of_the_board):
    matrix.append([x for x in input()])
    for column in range(size_of_the_board):
        if matrix[row][column] == "K":
            knights.append(([row, column]))
removed_knights = 0
positions_to_move = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

while True:
    max_hits = 0
    max_knights = [0, 0]
    for k_row, k_column in knights:
        hits = 0
        for move in positions_to_move:
            new_row = k_row + move[0]
            new_column = k_column + move[1]
            if 0 <= new_row < size_of_the_board and 0 <= new_column < size_of_the_board:
                if matrix[new_row][new_column] == "K":
                    hits += 1
        if hits > max_hits:
            max_hits = hits
            max_knights = [k_row, k_column]
    if max_hits == 0:
        break
    else:
        knights.remove(max_knights)
        matrix[max_knights[0]][max_knights[1]] = "0"
        removed_knights += 1

print(removed_knights)
