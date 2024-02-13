from collections import deque

time_to_complete = deque([int(el) for el in input().split()])
number_of_tasks = [int(el) for el in input().split()]

darth_vader_count = 0
thor_count = 0
big_blue_count = 0
small_yellow_count = 0

while time_to_complete and number_of_tasks:
    current_time = time_to_complete.popleft()
    current_task = number_of_tasks.pop()
    current_multiply = current_time * current_task
    if current_multiply in range(0, 61):
        darth_vader_count += 1
    elif current_multiply in range(61, 121):
        thor_count += 1
    elif current_multiply in range(121, 181):
        big_blue_count += 1
    elif current_multiply in range(181, 241):
        small_yellow_count += 1
    else:
        current_task -= 2
        time_to_complete.append(current_time)
        number_of_tasks.append(current_task)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {darth_vader_count}\nThor Ducky: {thor_count}\nBig Blue Rubber Ducky: {big_blue_count}\nSmall Yellow Rubber Ducky: {small_yellow_count}")