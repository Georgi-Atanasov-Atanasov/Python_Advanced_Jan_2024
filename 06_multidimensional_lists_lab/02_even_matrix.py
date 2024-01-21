rows_of_the_matrix = int(input())
matrix = []
for column in range(rows_of_the_matrix):
    info = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(info)

print(matrix)