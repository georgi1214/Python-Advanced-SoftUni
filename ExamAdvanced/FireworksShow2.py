from collections import deque

effect = deque([int(x) for x in input().split(', ') if int(x) > 0])
power = deque([int(x) for x in input().split(', ') if int(x) > 0])

palm_firework = 0
willow_firework = 0
crossette_firework = 0

success = False
while True:
    if not effect or not power:
        break

    first_effect = effect[0]
    last_power = power[-1]

    result = first_effect + last_power
    if result % 3 == 0 and result % 5 != 0:
        palm_firework += 1
        effect.popleft()
        power.pop()

    elif result % 5 == 0 and result % 3 != 0:
        willow_firework += 1
        effect.popleft()
        power.pop()

    elif result % 3 == 0 and result % 5 == 0:
        crossette_firework += 1
        effect.popleft()
        power.pop()

    else:
        removed_effect = effect.popleft()
        removed_effect -= 1
        if removed_effect > 0:
            effect.append(removed_effect)

    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        success = True
        break

if success:
    print('Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can't make the perfect firework show.")

if effect:
    print(f'Firework Effects left: {", ".join(str(e) for e in effect)}')

if power:
    print(f'Explosive Power left: {", ".join(str(p) for p in power)}')

print(f'Palm Fireworks: {palm_firework}')
print(f'Willow Fireworks: {willow_firework}')
print(f'Crossette Fireworks: {crossette_firework}')