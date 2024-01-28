rows = int(input())
matrix = [[int(x) for x in input().split()]for _ in range(rows)] # пълним матрицата

while True:
    command = input().split()
    if command[0] == 'END':
        break
    row, column, value = int(command[1]), int(command[2]), int(command[3])
    if row < 0 or row >= rows or column < 0 or column >= rows:
        print("Invalid coordinates")
        continue
    if command[0] == "Add":
        matrix[row][column] += value
    elif command[0] == "Subtract":
        matrix[row][column] -= value

for row in matrix:
    print(*row, sep=' ')



