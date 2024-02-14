from collections import deque

milligrams_of_caffeine = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(x) for x in input().split(", ")])
total_caffeine = 0

while energy_drinks and milligrams_of_caffeine:
    current_milligrams_of_caffeine = milligrams_of_caffeine.pop()
    current_energy_drinks = energy_drinks.popleft()
    current_caffeine = current_milligrams_of_caffeine * current_energy_drinks

    if total_caffeine + current_caffeine <= 300:
        total_caffeine += current_caffeine
    else:
        energy_drinks.append(current_energy_drinks)
        if total_caffeine - 30 >= 0:
            total_caffeine -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
