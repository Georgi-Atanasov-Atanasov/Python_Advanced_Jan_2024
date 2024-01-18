from collections import deque

string_expression = deque(input().split())

index = 0

while index < len(string_expression):
    element = string_expression[index]

    if element == '*':
        for _ in range(index - 1):
            string_expression.appendleft(int(string_expression.popleft()) * int(string_expression.popleft()))
    elif element == '/':
        for _ in range(index - 1):
            string_expression.appendleft(int(string_expression.popleft()) / int(string_expression.popleft()))
    elif element == '+':
        for _ in range(index - 1):
            string_expression.appendleft(int(string_expression.popleft()) + int(string_expression.popleft()))
    elif element == '-':
        for _ in range(index - 1):
            string_expression.appendleft(int(string_expression.popleft()) - int(string_expression.popleft()))
    if element in "*/+-":
        del string_expression[1]
        index = 1
    index += 1

print(int(string_expression[0] // 1))