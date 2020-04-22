def my_func(var_1, var_2):
    """ФУНКЦИЯ ДЕЛЕНИЯ
    Параметры функции:
    var_1 - делимое,
    var_2 - делитель,
    return - возвращает результат деления(частное)
    """
    try:
        return var_1 / var_2
    except ZeroDivisionError:
        print('Деление на ноль невозможно, пробуйте снова!')


while True:
    div_1 = int(input('Введите делимое число: '))
    div_2 = int(input('Введите делитель: '))
    result = my_func(div_1, div_2)

    if result != None:
        print(f'Ответ: {round(result, 3)}')
        break
