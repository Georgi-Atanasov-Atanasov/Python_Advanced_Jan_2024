battlefield = int(input())
matrix = []
position = []
mine_hits = 0
battle_cruiser_hits = 0

for row in range(battlefield):
    matrix.append(list(input()))
    for column in range(battlefield):
        if matrix[row][column] == "S":
            position = [row, column]
            matrix[position[0]][position[1]] = "-"

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

    if matrix[position[0]][position[1]] == "-":
        continue
    elif matrix[position[0]][position[1]] == "*":
        matrix[position[0]][position[1]] = "-"
        mine_hits += 1
        if mine_hits == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{position[0]}, {position[1]}]!")
            matrix[position[0]][position[1]] = "S"
            break
    elif matrix[position[0]][position[1]] == "C":
        matrix[position[0]][position[1]] = "-"
        battle_cruiser_hits += 1
        if battle_cruiser_hits == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            matrix[position[0]][position[1]] = "S"
            break

for row in matrix:
    print(f"{''.join(row)}")

