box_of_clothes = [int(x) for x in input().split()]
capacity_of_a_rack = int(input())
current_value = 0
number_of_racks = 1
box_of_clothes.reverse()
for clothes_value in box_of_clothes:
    current_value += int(clothes_value)
    if current_value > capacity_of_a_rack:
        number_of_racks += 1
        current_value = clothes_value

print(number_of_racks)

