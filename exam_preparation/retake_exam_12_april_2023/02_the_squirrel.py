size_of_the_field = int(input())
directions_to_move = input().split(", ")

position = []
matrix = []

hazelnuts_count = 0

for row in range(size_of_the_field):
    matrix.append(list(input()))
    for column in range(size_of_the_field):
        if matrix[row][column] == "s":
            position = [row, column]

for direction in directions_to_move:
    matrix[position[0]][position[1]] = "*"

    if direction == "up":
        position[0] -= 1
    elif direction == "down":
        position[0] += 1
    elif direction == "right":
        position[1] += 1
    elif direction == "left":
        position[1] -= 1

    if not (0 <= position[0] < size_of_the_field and 0 <= position[1] < size_of_the_field):
        print("The squirrel is out of the field.")
        break

    if matrix[position[0]][position[1]] == "h":
        hazelnuts_count += 1
        if hazelnuts_count == 3:
            print("Good job! You have collected all hazelnuts!")
            break

    if matrix[position[0]][position[1]] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break

else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts_count}")
