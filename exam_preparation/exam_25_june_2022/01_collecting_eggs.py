from collections import deque

egg_with_size = deque([int(x) for x in input().split(", ")])
paper_with_size = deque([int(x) for x in input().split(", ")])
box = 0
number_of_boxes = 0

while egg_with_size and paper_with_size:

    current_egg = egg_with_size.popleft()
    if current_egg <= 0:
        continue
    elif current_egg == 13:
        paper_with_size[0], paper_with_size[-1] = paper_with_size[-1], paper_with_size[0]
        continue
    current_paper = paper_with_size.pop()
    current_sum = current_egg + current_paper

    if current_sum <= 50:
        box += current_sum
        number_of_boxes += 1
        box = 0

if number_of_boxes > 0:
    print(f"Great! You filled {number_of_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if egg_with_size:
  print(f"Eggs left: {', '.join([str(x) for x in egg_with_size])}")

if paper_with_size:
    print(f"Pieces of paper left: {', '.join([str(x) for x in paper_with_size])}")