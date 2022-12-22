def det_next_position(d, r, c):
    if d == 'left':
        c -= 1
    elif d == 'right':
        c += 1
    elif d == 'up':
        r -= 1
    elif d == 'down':
        r += 1

    if r >= N:
        r = 0
    elif r < 0:
        r = (N - 1)
    if c >= N:
         c = 0
    elif c < 0:
         c = (N - 1)

    return r, c


N = int(input())
track = []
racing_number = input()
tunel_indexes = []
tunnel = []
car_row = 0
car_cow = 0

for r_ind in range(N):
    track.append(input().split())
    for c_ind in range(N):
        if track[r_ind][c_ind] == 'T':
            tunnel.append((r_ind, c_ind))
            tunel_indexes.append((r_ind, c_ind))

total_km = 0
while True:
    input_line = input()
    if input_line == 'End':
        print(f'Racing car {racing_number} DNF.')
        break
    direction = input_line
    car_row, car_cow = det_next_position(direction, car_row, car_cow)
    current_step = track[car_row][car_cow]
    if current_step == 'T':
        tunnel.remove((car_row, car_cow))
        car_row, car_cow = tunnel[0][0], tunnel[0][1]
        total_km += 20
        for tunel in tunel_indexes:
            track[tunel[0]][tunel[1]] = '.'
    elif current_step == 'F':
        print(f'Racing car {racing_number} finished the stage!')
        total_km += 10
        break
    total_km += 10

track[car_row][car_cow] = 'C'
print(f'Distance covered {total_km} km.')
for tunel in track:
    print(*tunel, sep='')




