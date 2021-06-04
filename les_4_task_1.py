from sys import argv

script_name, first_param, second_param, third_param = argv


def calc_func(arg_1, arg_2, arg_3):
    try:
        result = int(arg_1) * int(arg_2) + int(arg_3)
    except ValueError:
        return 'ОШИБКА! Введите значения в виде чисел!'
    return f'Заработная плата составляет: {result} руб.'


print('Имя скрипта: ', script_name)
print('Выработка в часах: ', first_param)
print('Ставка в час: ', second_param)
print('Премия: ', third_param)
print(calc_func(first_param, second_param, third_param))
