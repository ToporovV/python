def sum_func(*args):
    sum = 0
    stop = None
    for i in args:
        if i != 'Q':
            sum += int(i)
        else:
            stop = 'quit'

    return sum, stop


sum_all = 0

while True:
    numbers = input('Введите несколько цифр через пробел, для выхода нажмите "Q": ').upper().split(' ')
    sum, stop_point = sum_func(*numbers)
    sum_all += sum
    print(f'Общая сумма всех чисел равна: {sum_all}')

    if stop_point == 'quit':
        break
