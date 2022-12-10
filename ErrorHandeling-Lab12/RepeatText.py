try:
    string = input()
    multiply_times = int(input())

    result = string * multiply_times

    print(result)

except ValueError:
    print('Variable times must be an integer')