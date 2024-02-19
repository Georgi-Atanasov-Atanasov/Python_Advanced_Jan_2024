size_of_protected_airspace = int(input())

matrix = []
position = []
jetfighter_armor = 300
enemy_aircraft = 4


for row in range(size_of_protected_airspace):
    matrix.append(list(input()))
    for column in range(size_of_protected_airspace):
        if matrix[row][column] == "J":
            position = [row, column]
            matrix[row][column] = "-"

while enemy_aircraft != 0 or jetfighter_armor != 0:
    directions = input()

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
    elif matrix[position[0]][position[1]] == "R":
        matrix[position[0]][position[1]] = "-"
        jetfighter_armor = 300
    elif matrix[position[0]][position[1]] == "E":
        matrix[position[0]][position[1]] = "-"
        enemy_aircraft -= 1
        if enemy_aircraft == 0:
            print("Mission accomplished, you neutralized the aerial threat!")
            matrix[position[0]][position[1]] = "J"
            break
        else:
            jetfighter_armor -= 100
            if jetfighter_armor == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{position[0]}, {position[1]}]!")
                matrix[position[0]][position[1]] = "J"
                break

for row in matrix:
    print(f"{''.join(row)}")
