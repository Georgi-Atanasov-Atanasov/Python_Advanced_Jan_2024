player_start = input().split(", ")
first_player = player_start[0]
second_player = player_start[1]
turn = 0
first_lost_turn = False
second_lost_turn = False

SIZE = 6
matrix = []

for row in range(SIZE):
    matrix.append(input().split())

while True:
    turn += 1
    position = input()
    row = int(position[1])
    column = int(position[4])
    if turn % 2 != 0:
        if first_lost_turn == True:
            first_lost_turn = False
            continue
        first_player_position = [row, column]
        if matrix[row][column] == "E":
            print(f"{first_player} found the Exit and wins the game!")
            break
        elif matrix[row][column] == "T":
            print(f"{first_player} is out of the game! The winner is {second_player}.")
            break
        elif matrix[row][column] == "W":
            print(f"{first_player} hits a wall and needs to rest.")
            first_lost_turn = True

    else:
        second_player_position = [row, column]
        if second_lost_turn == True:
            second_lost_turn = False
            continue
        if matrix[row][column] == "E":
            print(f"{second_player} found the Exit and wins the game!")
            break
        elif matrix[row][column] == "T":
            print(f"{second_player} is out of the game! The winner is {first_player}.")
            break
        elif matrix[row][column] == "W":
            print(f"{second_player} hits a wall and needs to rest.")
            second_lost_turn = True
        elif matrix[row][column] == ".":
            continue
