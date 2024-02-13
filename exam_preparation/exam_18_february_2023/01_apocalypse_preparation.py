from collections import deque

textile = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

MED_KIT_VALUE = 100
item_list = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100
}

created_items = {}

while textile and medicaments:
    current_textile = textile.popleft()
    current_medicament = medicaments.pop()
    current_sum = current_textile + current_medicament

    if current_sum in item_list.values():
        index_value = list(item_list.values()).index(int(current_sum))
        current_key = list(item_list)[index_value]
        if current_key in created_items:
            created_items[current_key] += 1
        else:
            created_items[current_key] = 1
    elif current_sum > MED_KIT_VALUE:
        current_key = "MedKit"
        left_sum = current_sum - MED_KIT_VALUE
        if "MedKit" in created_items:
            created_items[current_key] += 1
        else:
            created_items[current_key] = 1
        current_medicament = medicaments.pop()
        medicaments.append(current_medicament + left_sum)
    else:
        current_medicament += 10
        medicaments.append(current_medicament)

if not textile and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textile:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")


if created_items:
    for key, value in sorted(created_items.items(), key=lambda x: (-x[1], x[0])):
        print(f"{key} - {value}")

if medicaments:
    current_list = []
    for medicament in medicaments:
        current_list.append(medicament)
    print(f"Medicaments left: {', '.join(str(x) for x in current_list[::-1])}")

if textile:
    print(f"Textiles left: {', '.join([str(x) for x in textile])}")
