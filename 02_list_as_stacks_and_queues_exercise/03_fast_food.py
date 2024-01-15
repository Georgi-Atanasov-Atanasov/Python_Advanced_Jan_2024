from collections import deque

daily_food_quantity = int(input())
orders = deque([int(x) for x in input().split()])
print(max(orders))
for order in orders.copy():
    if order > daily_food_quantity:
      print(f"Orders left:", *orders)
      break
    else:
      daily_food_quantity -= order
      orders.popleft()
else:
   print("Orders complete")



