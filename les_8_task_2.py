class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    dividend = int(input('Введите делимое число: '))
    divider = int(input('Введите делитель: '))

    if divider == 0:
        raise OwnError('Деление на ноль невозможно.')
except ValueError:
    print('Введите число.')
except OwnError as err:
    print(err)
else:
    print(f'Ваш результат: {round(dividend / divider, 3)}')
