N, M = [int(x) for x in input().split(",")]

starting_cheese_pieces = 0
collected_cheese = 0
matrix = []
position = []
starting_position = []

for row in range(N):
    matrix.append(list(input()))
    for column in range(M):
        if matrix[row][column] == "M":
            position = [row, column]
            starting_position = position.copy()
            matrix[row][column] = "*"
        elif matrix[row][column] == "C":
            starting_cheese_pieces += 1


while True:
    directions = input()

    previous_position = position.copy()
    if directions == "danger":
        if collected_cheese < starting_cheese_pieces:
            print("Mouse will come back later!")
        break

    elif directions == "up":
        position[0] -= 1
    elif directions == "down":
        position[0] += 1
    elif directions == "right":
        position[1] += 1
    elif directions == "left":
        position[1] -= 1

    if not (0 <= int(position[0]) < N and 0 <= int(position[1]) < M):
        print("No more cheese for tonight!")
        position = previous_position
        matrix[position[0]][position[1]] = "M"
        break

    if matrix[position[0]][position[1]] == "*":
        continue

    elif matrix[position[0]][position[1]] == "C":
        matrix[position[0]][position[1]] = "*"
        collected_cheese += 1
        if collected_cheese == starting_cheese_pieces:
            matrix[position[0]][position[1]] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    elif matrix[position[0]][position[1]] == "@":
        position = previous_position
        continue

    elif matrix[position[0]][position[1]] == "T":
        matrix[position[0]][position[1]] = "M"
        print("Mouse is trapped!")
        break

for row in matrix:
    print(f"{''.join(row)}")
