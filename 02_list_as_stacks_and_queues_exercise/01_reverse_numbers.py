from collections import deque

# numbers = deque(input().split())
# numbers.reverse()
# print(*numbers)


# second solution
numbers = deque(input().split())
for number in range(len(numbers)):
    print(numbers.pop(), end=' ')