rows, columns = [int(x) for x in input().split()]

starting_letter = ord('a')

for row in range(starting_letter, starting_letter + rows):
    for column in range(row, row + columns):
        print(chr(row), chr(column), chr(row), sep="", end=" ")

    print()