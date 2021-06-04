def my_func(x, y):
    return round(x ** y, 5)


def my_func_2(x, y):
    i = 1
    result = 1 / x
    while i < abs(y):
        result = result * (1 / x)
        i += 1
    return round(result, 5)


print(f'Первый способ с помощью оператора "**": {my_func(3, -8)}')
print(f'Второй способ с использованием цикла: {my_func_2(2, -5)}')