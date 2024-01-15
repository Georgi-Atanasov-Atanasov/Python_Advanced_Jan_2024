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
