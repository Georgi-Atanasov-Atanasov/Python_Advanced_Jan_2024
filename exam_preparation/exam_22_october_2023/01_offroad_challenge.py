from collections import deque

initial_fuel = [int(x) for x in input().split()]
additional_consumption_index = deque(int(x) for x in input().split())
needed_fuel = deque(int(x) for x in input().split())
altitude_counter = 0
reached_altitudes = []

while initial_fuel and additional_consumption_index and needed_fuel:
    current_fuel = initial_fuel.pop()
    current_additional_consumption_index = additional_consumption_index.popleft()
    current_needed_fuel = needed_fuel.popleft()
    current_result = current_fuel - current_additional_consumption_index
    altitude_counter += 1

    if current_result >= current_needed_fuel:
        reached_altitudes.append(f"Altitude {altitude_counter}")
        print(f"John has reached: Altitude {altitude_counter}")
    else:
        print(f"John did not reach: Altitude {altitude_counter}")
        break

if len(reached_altitudes) == 0:
    print("John failed to reach the top. John didn't reach any altitude.")
elif 0 < len(reached_altitudes) < 4:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(reached_altitudes)}")
elif len(reached_altitudes) == 4:
    print("John has reached all the altitudes and managed to reach the top!")


# from collections import deque
#
# initial_fuel = [int(ch) for ch in input().split(' ')]
# additional_consumption_index = deque(int(ch) for ch in input().split(' '))
# amount_of_fuel_needed = deque(int(ch) for ch in input().split(' '))
# altitude_counter = 0
# reached_altitude = []
#
# while initial_fuel and additional_consumption_index and amount_of_fuel_needed:
#     last_fuel = initial_fuel.pop()
#     first_index = additional_consumption_index.popleft()
#     element_needed = amount_of_fuel_needed.popleft()
#     result = last_fuel - first_index
#     altitude_counter += 1
#
#     if result < element_needed:
#         print(f"John did not reach: Altitude {altitude_counter}")
#         break
#
#     reached_altitude.append(f"Altitude {altitude_counter}")
#     print(f"John has reached: Altitude {altitude_counter}")
#
# if 0 < len(reached_altitude) < 4:
#     print("John failed to reach the top.")
#     print(f"Reached altitudes: {', '.join(reached_altitude)}")
#
# if len(reached_altitude) == 0:
#     print("John failed to reach the top.\nJohn didn't reach any altitude.")
#
# if len(reached_altitude) == 4:
#     print("John has reached all the altitudes and managed to reach the top!")