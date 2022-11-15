numbers = input().split(' ')

result = ''

for i in range(len(numbers)):
    result += numbers.pop() + ' '
print(result)