#83 / 100
N, M = [int(x) for x in input().split()]

matrix = []
position = []
starting_position = []
for row in range(N):
    matrix.append(list(input()))
    for column in range(M):
        if matrix[row][column] == "B":
            position = [row, column]
            starting_position = position.copy()

while True:
    directions = input()

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
        print("The delivery is late. Order is canceled.")
        position = previous_position
        matrix[starting_position[0]][starting_position[1]] = " "
        break

    if matrix[position[0]][position[1]] == "*":
        position = previous_position
        continue

    elif matrix[position[0]][position[1]] == "P":
        matrix[position[0]][position[1]] = "R"
        print("Pizza is collected. 10 minutes for delivery.")

    elif matrix[position[0]][position[1]] == "A":
        matrix[position[0]][position[1]] = "P"
        print("Pizza is delivered on time! Next order...")
        break

    elif matrix[position[0]][position[1]] == "-":
        matrix[position[0]][position[1]] = "."
        continue

for row in matrix:
    print(f"{''.join(row)}")