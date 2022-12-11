num_list = [int(x) for x in input().split(', ')]
result = 1


for i in range(len(num_list)):
    number = num_list[i]
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number


print(result)