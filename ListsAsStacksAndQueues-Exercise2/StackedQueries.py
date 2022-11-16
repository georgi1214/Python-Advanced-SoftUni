n = int(input())
stack = []

for i in range(n):
    command = input()

    if command[0] == '1':
        stack.append(int(command.split()[1]))
    elif command[0] == '2':
        stack.pop()
    elif command[0] == '3':
        print(max(stack))
    elif command[0] == '4':
        print(min(stack))

while stack:
    print((str(stack.pop())) + ', ', end='')