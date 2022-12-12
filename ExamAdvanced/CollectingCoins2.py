def validate_step(r, c):
    if r >= SIZE:
        r = 0
    elif r < 0:
        r = (SIZE - 1)
    if c >= SIZE:
        c = 0
    elif c < 0:
        c = (SIZE - 1)
    return r, c


def get_next_position(direction, r, c):
    if direction == 'left':
        return validate_step(r, c - 1)
    elif direction == 'right':
        return validate_step(r, c + 1)
    elif direction == 'up':
        return validate_step(r - 1, c)
    elif direction == 'down':
        return validate_step(r + 1, c)


SIZE = int(input())
matrix = []
row, col = 0, 0

for row_index in range(SIZE):
    matrix.append(input().split())
    for col_index in range(SIZE):
        if matrix[row_index][col_index] == 'P':
            row, col = row_index, col_index

points = []
path = [[row, col]]
while True:
    command = input()
    if command == "":
        break
    if command not in ['up', 'down', 'left', 'right']:
        continue

    row, col = get_next_position(command, row, col)
    current_step = matrix[row][col]

    path.append([row, col])

    if current_step == 'X':
        print(f"Game over! You've collected {sum(points) // 2} coins.")
        break

    if not current_step.isalpha():
        points.append(int(current_step))
        matrix[row][col] = '0'

    if sum(points) >= 100:
        print(f"You won! You've collected {sum(points)} coins.")
        break

print('Your path:')
for step in path:
    print(step)