from collections import deque
tools = deque([int(x) for x in input().split()])
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances and challenges:
    current_tool = tools.popleft()
    current_substance = substances.pop()
    multiplied_value = current_tool * current_substance
    if multiplied_value in challenges:
        challenges.remove(multiplied_value)
    else:
        current_tool += 1
        tools.append(current_tool)
        current_substance -= 1
        if current_substance > 0:
            substances.append(current_substance)

if challenges:
    if not substances or not tools:
        print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")

if tools:
    print(', '.join(str(x) for x in tools))
if substances:
    print(', '.join(str(x) for x in substances))
if challenges:
    print(', '.join(str(x) for x in challenges))














