from collections import deque

armor_of_monsters = deque([int(x) for x in input().split(",")])
soldiers_strike = [int(x) for x in input().split(",")]

killed_monsters = 0

while armor_of_monsters and soldiers_strike:
    current_armor = armor_of_monsters.popleft()
    current_strike = soldiers_strike.pop()
    if current_strike >= current_armor:
        killed_monsters += 1
        current_strike -= current_armor
        if soldiers_strike:
            last_element = soldiers_strike.pop()
            soldiers_strike.append(last_element + current_strike)
        else:
            if current_strike > 0:
               soldiers_strike.append(current_strike)
    else:
        current_armor -= current_strike
        armor_of_monsters.append(current_armor)

if not armor_of_monsters:
    print("All monsters have been killed!")
if not soldiers_strike:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")










