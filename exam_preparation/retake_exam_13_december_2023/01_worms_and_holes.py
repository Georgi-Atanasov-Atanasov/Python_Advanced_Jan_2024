from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())
starting_worms = len(worms)
matches_count = 0

while worms and holes:
    current_worm = worms.pop()
    current_hole = holes.popleft()
    if current_hole == current_worm:
        matches_count += 1
    else:
        current_worm -= 3
        if current_worm > 0:
           worms.append(current_worm)

if matches_count == 0:
    print("There are no matches.")
else:
    print(f"Matches: {matches_count}")

if not worms and starting_worms == matches_count:
    print("Every worm found a suitable hole!")
elif not worms and starting_worms != matches_count:
    print("Worms left: none")
elif worms:
    print(f"Worms left: {', '.join(str(x) for x in worms)}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(str(x) for x in holes)}")