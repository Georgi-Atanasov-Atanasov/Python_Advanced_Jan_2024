first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

for _ in range(int(input())):
    first_command, second_command, *data = input().split()

    command = first_command + " " + second_command

    if command == "Add First":
        [first_set.add(int(element)) for element in data]   #first_set.update(second_set)
    elif command == "Add Second":
        [second_set.add(int(element)) for element in data]
    elif command == "Remove First":
        [first_set.discard(int(element)) for element in data]
    elif command == "Remove Second":
        [second_set.discard(int(element)) for element in data]
    elif command == "Check Subset":
        if second_set < first_set:
            print(True)
        else:
            print(False)
        #alternative print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")


## second option with lambda functions
# first_set = set(int(x) for x in input().split())
# second_set = set(int(x) for x in input().split())
#
# functions = {
#     "Add First": lambda x: [first_set.add(int(el)) for el in x],  # first_set.update(second_set)
#     "Add Second": lambda x: [second_set.add(int(el)) for el in x],
#     "Remove First": lambda x: [first_set.discard(int(el)) for el in x],
#     "Remove Second": lambda x: [second_set.discard(int(el)) for el in x],
#     "Check Subset": lambda x: print(first_set.issubset(second_set) or second_set.issubset(first_set)),
# }
#
# for _ in range(int(input())):
#     first_command, second_command, *data = input().split()
#
#     command = first_command + " " + second_command
#
#     functions[command](data)
#
# print(*sorted(first_set), sep=", ")
# print(*sorted(second_set), sep=", ")