from collections import deque

pumps_qty = int(input())


def check(stations_qty):
    stations_data = deque()

    for _ in range(stations_qty):
        stations = [int(el) for el in input().split(" ")]
        stations_data.append(stations)

    for station in range(stations_qty):
        tank = 0
        is_ok = True
        for s in range(stations_qty):
            tank += stations_data[s][0]-stations_data[s][1]
            if tank < 0:
                is_ok = False
                stations_data.append(stations_data.popleft())
                break
        if is_ok:
            print(f"{station}")
            break


check(pumps_qty)