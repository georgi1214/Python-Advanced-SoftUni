import math


def is_inside(some_row, some_col):  # validating if cell is inside the matrix.
    return 0 <= some_row < size and 0 <= some_col < size


def get_next_position_func(direction, row, col):
    if direction == 'up':
        return row - 1, col
    elif direction == 'down':
        return row + 1, col
    elif direction == 'left':
        return row, col - 1
    elif direction == 'right':
        return row, col + 1


size = int(input())
p_row = 0
p_col = 0
matrix = []
for row_index in range(size):
    matrix.append(input().split())
    for col_index in range(size):
        if matrix[row_index][col_index] == 'P':
            p_row = row_index
            p_col = col_index

wall_hit = False
coins = 0
path = [[p_row, p_col]]

while True:
    command = input()
    matrix[p_row][p_col] = '0'
    next_row, next_col = get_next_position_func(command, p_row, p_col)
    path.append([next_row, next_col])
    if is_inside(next_row, next_col):

        if matrix[next_row][next_col] != 'X':
            coins += int(matrix[next_row][next_col])
            matrix[next_row][next_col] = '0'
            p_row, p_col = next_row, next_col

        else:
            wall_hit = True
            break

    else:
        if command == 'down':
            p_row = next_row - size
        elif command == 'left':
            p_col = next_col + size
        elif command == 'up':
            p_row = next_row + size
        elif command == 'right':
            p_col = next_col - size
        path.pop(-1)
        path.append([p_row, p_col])
        if str(matrix[p_row][p_col]).isdigit() and matrix[p_row][p_col] != 'X':
            coins += int(matrix[p_row][p_col])
            matrix[p_row][p_col] = '0'
        else:
            wall_hit = True
            break

    if coins >= 100 or wall_hit:
        break

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    if wall_hit:
        coins /= 2
        print(f"Game over! You've collected {math.floor(coins)} coins.")

print('Your path:')
print(*path, sep='\n')
