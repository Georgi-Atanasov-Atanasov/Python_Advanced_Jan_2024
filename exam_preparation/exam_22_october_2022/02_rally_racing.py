size_of_the_matrix = int(input())
starting_number = input()

matrix = []
kilometers_passed = 0
position = [0, 0]
T1_position = []
T2_position = []

for row in range(size_of_the_matrix):
    row_data = input().split()
    matrix.append(row_data)
    for column in range(size_of_the_matrix):
        if matrix[row][column] == "T":
            if len(T1_position) == 0:
                T1_position = [row, column]
            else:
                T2_position = [row, column]

while True:
    command = input()

    if command == 'up':
        position[0] -= 1
        kilometers_passed += 10
    elif command == 'down':
        position[0] += 1
        kilometers_passed += 10
    elif command == 'left':
        position[1] -= 1
        kilometers_passed += 10
    elif command == 'right':
        position[1] += 1
        kilometers_passed += 10
    if command == "End":
        print(f"Racing car {starting_number} DNF.")
        matrix[position[0]][position[1]] = "C"
        break

    if matrix[position[0]][position[1]] == "T":
        kilometers_passed += 20
        matrix[position[0]][position[1]] = "."
        if position == T1_position:
            position = T2_position
        else:
            position = T1_position
        matrix[position[0]][position[1]] = "."

    elif matrix[position[0]][position[1]] == "F":
        print(f"Racing car {starting_number} finished the stage!")
        matrix[position[0]][position[1]] = "C"
        break

print(f"Distance covered {kilometers_passed} km." )
for row in matrix:
    print(f"{''.join(row)}")






