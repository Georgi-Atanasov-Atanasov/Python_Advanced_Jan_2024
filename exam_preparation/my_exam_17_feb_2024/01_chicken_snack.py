from collections import deque

amount_of_money = [int(el) for el in input().split()]
prices_of_food = deque([int(el) for el in input().split()])
starting_number_of_ffods = len(prices_of_food)

number_of_eaten_foods = 0

while amount_of_money and prices_of_food:
    current_amount_of_money = amount_of_money.pop()
    current_price = prices_of_food.popleft()
    if current_amount_of_money == current_price:
        number_of_eaten_foods += 1
    elif current_amount_of_money > current_price:
        change = current_amount_of_money - current_price
        number_of_eaten_foods += 1
        if len(amount_of_money) > 0:
          next_amount_of_money = amount_of_money.pop()
          amount_of_money.append(next_amount_of_money + change)
    elif current_amount_of_money < current_price:
        continue


if number_of_eaten_foods >= 4:
    print(f"Gluttony of the day! Henry ate {number_of_eaten_foods} foods.")
elif 4 >= number_of_eaten_foods > 0:
    if number_of_eaten_foods == 1:
        print(f"Henry ate: {number_of_eaten_foods} food.")
    else:
        print(f"Henry ate: {number_of_eaten_foods} foods.")
elif number_of_eaten_foods == 0:
    print("Henry remained hungry. He will try next weekend again.")

