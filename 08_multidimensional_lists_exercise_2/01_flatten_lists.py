numbers = [num.split() for num in input().split("|")]

for number in numbers[::-1]:
    [print(chart, end=" ") for chart in number]
