N, M = [int(x) for x in input().split()]

matrix = []
position = []
previous_position = []

touches = 0
moves = 0
TOTAL_PLAYERS = 3
game_over = False

for row in range(N):
    matrix.append(input().split())
    for column in range(M):
        if matrix[row][column] == "B":
            position = [row, column]
            matrix[position[0]][position[1]] = "-"

while True:
    directions = input()
    if directions == "Finish":
        game_over = True
        break

    previous_position = position.copy()
    if directions == "up":
        position[0] -= 1
    elif directions == "down":
        position[0] += 1
    elif directions == "right":
        position[1] += 1
    elif directions == "left":
        position[1] -= 1


    if not (0 <= int(position[0]) < N and 0 <= int(position[1]) < M):
        position = previous_position
        continue
    elif matrix[position[0]][position[1]] == "O":
        position = previous_position
        continue
    elif matrix[position[0]][position[1]] == "P":
        touches += 1
        moves += 1
        matrix[position[0]][position[1]] = "-"
    elif matrix[position[0]][position[1]] == "-":
        moves += 1

    if touches == TOTAL_PLAYERS:
        game_over = True
        break

if game_over == True:
    print("Game over!")
    print(f"Touched opponents: {touches} Moves made: {moves}")
