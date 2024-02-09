size = int(input())

matrix = []
position = []
amount = 100
jackpot = False

for row in range(size):
    row_data = list(input())
    matrix.append(row_data)
    for col in range(size):
        if matrix[row][col] == "G":
            position = [row, col]

while True:
    directions = input()

    if directions == "end":
        break
    matrix[position[0]][position[1]] = "-"
    if directions == "up":
        position[0] -= 1
    elif directions == "down":
        position[0] += 1
    elif directions == "right":
        position[1] += 1
    elif directions == "left":
        position[1] -= 1


    if matrix[position[0]][position[1]] == "W":
        amount += 100
    elif matrix[position[0]][position[1]] == "P":
        amount -= 200
    elif matrix[position[0]][position[1]] == "J":
        amount += 100000
        jackpot = True
        matrix[position[0]][position[1]] = "G"
        break
    matrix[position[0]][position[1]] = "G"

    if not (0 <= int(position[0]) < size and 0 <= int(position[1]) < size) or amount <= 0:
        print("Game over! You lost everything!")
        exit()

if jackpot:
    print("You win the Jackpot!")
    print(f"End of the game. Total amount: {amount}$")
    [print(*row, sep='') for row in matrix]
else:
    print(f"End of the game. Total amount: {amount}$")
    [print(*row, sep='') for row in matrix]