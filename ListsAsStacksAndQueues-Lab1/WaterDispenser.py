from collections import deque

people = deque()

total_water = int(input())

while True:
    line = input()
    if line == 'Start':
        break
    people.append(line)

while True:
    line = input()
    if line == 'End':
        break

    line_args = line.split()
    if len(line_args) == 2:
        total_water += int(line_args[1])

    else:
        liters = int(line_args[0])
        person = people.popleft()
        if liters > total_water:
            print(f"{person} must wait")
        else:
            print(f'{person} got water')
            total_water -= liters
print(f'{total_water} liters left')