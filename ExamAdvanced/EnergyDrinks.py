from collections import deque

milligrams_caffeine = deque(list(map(int, input().split(', '))))
energy_drinks = deque(list(map(int, input().split(', '))))

stamat_caffeine = 0
max_caffeine = 300

while milligrams_caffeine and energy_drinks:

    if milligrams_caffeine and energy_drinks:
        last_caffeine = milligrams_caffeine.pop()
        first_drink = energy_drinks.popleft()
        sum_of_caffeine = last_caffeine * first_drink

        if sum_of_caffeine + stamat_caffeine <= max_caffeine:
            stamat_caffeine += sum_of_caffeine
        elif stamat_caffeine < max_caffeine:
            energy_drinks.append(first_drink)
            if stamat_caffeine != 0:
                stamat_caffeine -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_caffeine} mg caffeine.")