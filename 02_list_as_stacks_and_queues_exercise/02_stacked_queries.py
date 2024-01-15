numbers = []

for number in range(int(input())):
    data = input().split()
    if data[0] == "1":
        numbers.append(int(data[1]))
    elif data[0] == "2":
        if numbers:
            numbers.pop()
    elif data[0] == "3":
        if numbers:
            print(max(numbers))
    elif data[0] == "4":
        if numbers:
            print(min(numbers))
numbers.reverse()
print(*numbers, sep=", ")


# numbers = []
#
# def sum(a, b):
#     return  a + b
#
# map_functions = {
#     "1": lambda x: numbers.append(x[1]),
#     "2": lambda x: numbers.pop() if numbers else None,
#     "3": lambda x: print(max(numbers)) if numbers else None,
#     "4": lambda x: print(min(numbers)) if numbers else None,
# }
#
# for _ in range(int(input())):
#     numbers_data = input().split()  # "1 97" -> ["1", "97"] -> [1, 97]
#     command = numbers_data[0]  # 1
#     map_functions[command](numbers_data)
#
# numbers.reverse()
#
# print(*numbers, sep=", ")