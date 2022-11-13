from collections import deque

food_qty = int(input())
orders = deque(int(el) for el in input().split(" "))


def print_result(queue):
    if queue:
        print(f"Orders left: {' '.join([str(el) for el in queue])}")
    else:
        print("Orders complete")


def food_check(food, queue):
    print(max(queue))

    while queue:
        f = queue.popleft()
        if f <= food:
            food -= f
        else:
            queue.appendleft(f)
            break

    print_result(queue)


food_check(food_qty, orders)